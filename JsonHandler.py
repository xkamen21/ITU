# Subject: ITU
# School:  Faculty of Information Technology, Brno University of Technology
# Authors: Boris Burkalo
#          Daniel Kamenický
#          Jan Klusáček
#
from ITUsportsTracker import *

class JsonFunctions(MainWindow):

    def SaveUserData(self):
        if not os.path.isfile("data"):
            os.mkdir("./data")
        data = {}
        data['First_name'] = self.registration_name_edit.text()
        data['Last_name'] = self.registration_surname_edit.text()
        data['Height'] = self.registration_height_edit.text()
        data['Weight'] = self.registration_weight_edit.text()
        data['Profile_picture'] = ""
        with open("data/credential_itu.json", "w+") as write_file:
            json.dump(data, write_file)
        goals = {}
        goals['Running'] = 10
        goals['Skating'] = 10
        goals['Walking'] = 10
        goals['Cycling'] = 10
        with open("data/goals_itu.json", "w+") as write_file:
            json.dump(goals, write_file)

    def ChangeUserData(self, name, surname, height, weight):
        with open("data/credential_itu.json", "r") as read_file:
            data = json.load(read_file)
        if name != None:
            data['First_name'] = name
        if surname != None:
            data['Last_name'] = surname
        if height != None:
            data['Height'] = height
        if weight != None:
            data['Weight'] = weight
        with open("data/credential_itu.json", "w+") as write_file:
            json.dump(data, write_file)


    def ChangeGoalsData(self, type, value):
        with open("data/goals_itu.json", "r") as read_file:
            data = json.load(read_file)
        if type == 'Běh':
            data['Running'] = value
        if type == 'Bruslení':
            data['Skating'] = value
        if type == 'Chůze':
            data['Walking'] = value
        if type == 'Cyklistika':
            data['Cycling'] = value
        with open("data/goals_itu.json", "w+") as write_file:
            json.dump(data, write_file)

    def SetUserData(self):
        with open("data/credential_itu.json", "r") as read_file:
            data = json.load(read_file)
        self.profile_name_label.setText(data['First_name'])
        self.profile_surname_label.setText(data['Last_name'])
        self.profile_height_label.setText(data['Height'])
        self.profile_weight_label.setText(data['Weight'])
        self.name_edit.setText(data['First_name'])
        self.surname_edit.setText(data['Last_name'])
        self.height_edit.setText(data['Height'])
        self.weight_edit.setText(data['Weight'])
        if data['Profile_picture'] != "":
            self.user_foto_label.setPixmap(QPixmap(data['Profile_picture']))
            self.profile_foto_label.setPixmap(QPixmap(data['Profile_picture']))

        with open("data/goals_itu.json", "r") as read_file:
            goals = json.load(read_file)
        self.label_13.setText(str(goals['Running']))
        self.label_15.setText(str(goals['Skating']))
        self.label_17.setText(str(goals['Walking']))
        self.label_19.setText(str(goals['Cycling']))

        initials = data['First_name'][0].upper() + data['Last_name'][0].upper()
        self.profile_label.setText(initials)
        JsonFunctions.actualizateGoals(self)

    def SaveProfilePicture(self, path):
        with open("data/credential_itu.json", "r") as read_file:
            data = json.load(read_file)
        data['Profile_picture'] = path
        with open("data/credential_itu.json", "w+") as write_file:
            json.dump(data, write_file)


    def SaveActivityData(self, sport, time):
        if not os.path.exists("data/data_itu.json"):
            data = {}
            data['Excercises'] = []
        else:
            with open("data/data_itu.json", "r") as read_file:
                data = json.load(read_file)
        data['Excercises'].append({
            'Sport': '',
            'Day': '',
            'Week': '',
            'Day_in': '',
            'Month': '',
            'Year': '',
            'Time': ''
        })
        weekday = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
        data['Excercises'][len(data['Excercises'])-1]['Sport'] = sport
        data['Excercises'][len(data['Excercises'])-1]['Day'] = datetime.datetime.now().day
        data['Excercises'][len(data['Excercises'])-1]['Week'] = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day).isocalendar()[1]
        data['Excercises'][len(data['Excercises'])-1]['Day_in'] = weekday.weekday()
        data['Excercises'][len(data['Excercises'])-1]['Month'] = datetime.datetime.now().month
        data['Excercises'][len(data['Excercises'])-1]['Year'] = datetime.datetime.now().year
        data['Excercises'][len(data['Excercises'])-1]['Time'] = time
        with open("data/data_itu.json", "w+") as write_file:
            json.dump(data, write_file)

    def actualizateGoals(self):
        run = 0
        walk = 0
        skate = 0
        cycle = 0
        if os.path.exists("data/data_itu.json"):
            with open("data/data_itu.json", "r") as read_file:
                data = json.load(read_file)
            for item in data['Excercises']:
                if datetime.datetime.now().year == item['Year']:
                    if datetime.datetime.now().month == item['Month']:
                        if datetime.datetime.now().day == item['Day']:
                            if item['Sport'] == 'Běh':
                                run += item['Time']
                            elif item['Sport'] == 'Chůze':
                                walk += item['Time']
                            elif item['Sport'] == 'Bruslení':
                                skate += item['Time']
                            else:
                                cycle += item['Time']
            with open("data/goals_itu.json", "r") as read_file:
                goals = json.load(read_file)
            if goals['Running'] != 0:
                if round((100/int(goals['Running']))*run) > 100:
                    self.run_progressBar.setValue(100)
                else:
                    self.run_progressBar.setValue(round((100/int(goals['Running']))*run))
            else:
                self.run_progressBar.setValue(0)
            if goals['Walking'] != 0:
                if round((100/int(goals['Walking']))*walk) > 100:
                    self.walk_progressBar.setValue(100)
                else:
                    self.walk_progressBar.setValue(round((100/int(goals['Walking']))*walk))
            else:
                self.walk_progressBar.setValue(0)
            if goals['Skating'] != 0:
                if round((100/int(goals['Skating']))*skate) > 100:
                    self.skate_progressBar.setValue(100)
                else:
                    self.skate_progressBar.setValue(round((100/int(goals['Skating']))*skate))
            else:
                self.skate_progressBar.setValue(0)
            if goals['Cycling'] != 0:
                if round((100/int(goals['Cycling']))*cycle) > 100:
                    self.cycle_progressBar.setValue(100)
                else:
                    self.cycle_progressBar.setValue(round((100/int(goals['Cycling']))*cycle))
            else:
                self.cycle_progressBar.setValue(0)
        else:
            self.run_progressBar.setValue(0)
            self.walk_progressBar.setValue(0)
            self.skate_progressBar.setValue(0)
            self.cycle_progressBar.setValue(0)

    def setGraph(self, sport):
        weekX = [1,2,3,4,5,6,7]
        weekY = [0,0,0,0,0,0,0]
        monthDays = {1:'31', 2:'29', 3:'31', 4:'30', 5:'31', 6:'30', 7:'31', 8:'31', 9:'30', 10:'31', 11:'30', 12:'31'}
        monthX = []
        monthY = []
        yearX = [1,2,3,4,5,6,7,8,9,10,11,12]
        yearY = [0,0,0,0,0,0,0,0,0,0,0,0]

        for x in range(int(monthDays[datetime.datetime.now().month])):
            monthY.append(0)
            monthX.append(x+1)

        if os.path.exists("data/data_itu.json"):
            with open("data/data_itu.json", "r") as read_file:
                data = json.load(read_file)
            for item in data['Excercises']:
                if item['Sport'] == sport:
                    if item['Week'] == datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day).isocalendar()[1]:
                        weekY[int(item['Day_in'])] += item['Time']
                    if item['Month'] == datetime.datetime.now().month:
                        monthY[int(item['Day']-1)] += item['Time']
                    if item['Year'] == datetime.datetime.now().year:
                        yearY[int(item['Month'])-1] += item['Time']

        pen = pg.mkPen(color=(115, 210, 22), width = 3)

        self.week_tab.clear()
        self.month_tab.clear()
        self.year_tab.clear()

        self.week_tab.showGrid(x=True, y=True)
        self.month_tab.showGrid(x=True, y=True)
        self.year_tab.showGrid(x=True, y=True)

        self.week_tab.setLabel('left', "<span style=\"color:rgb(0, 0, 0);font-size:20px\">Čas (min)</span>")
        self.week_tab.setLabel('bottom', "<span style=\"color:rgb(0, 0, 0);font-size:20px\">Den</span>")

        self.month_tab.setLabel('left', "<span style=\"color:rgb(0, 0, 0);font-size:20px\">Čas (min)</span>")
        self.month_tab.setLabel('bottom', "<span style=\"color:rgb(0, 0, 0);font-size:20px\">Měsíc</span>")

        self.year_tab.setLabel('left', "<span style=\"color:rgb(0, 0, 0);font-size:20px\">Čas (min)</span>")
        self.year_tab.setLabel('bottom', "<span style=\"color:rgb(0, 0, 0);font-size:20px\">Rok</span>")

        self.week_tab.plot(weekX, weekY, pen=pen)
        self.month_tab.plot(monthX, monthY, pen=pen)
        self.year_tab.plot(yearX, yearY, pen=pen)
