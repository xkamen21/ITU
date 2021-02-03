# Subject: ITU
# School:  Faculty of Information Technology, Brno University of Technology
# Authors: Boris Burkalo
#          Daniel Kamenický
#          Jan Klusáček
#
import sys, os, platform, json, shutil, datetime
from PyQt5 import QtCore, QtWidgets, QtGui, uic
import pyqtgraph as pg
from pyqtgraph import PlotWidget
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

from imports import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #sets starting size of window
        self.resize(QSize(100, 720))

        #sets graph background
        self.week_tab.setBackground((44, 49, 60))
        self.month_tab.setBackground((44, 49, 60))
        self.year_tab.setBackground((44, 49, 60))

        #sets buttons
        GuiFunctions.ActivateTopBarButtons(self)
        GuiFunctions.ActivateMenuButtons(self)

        #sets the program path in the upper bar
        self.file_path_label.setText(os.getcwd())

        #init timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.time)

        #init time params
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        #connect timer buttons
        self.timer_start_button.clicked.connect(self.startTime)
        self.timer_stop_button.clicked.connect(self.stopTime)
        self.timer_reset_button.clicked.connect(self.resetTime)
        self.timer_save_button.clicked.connect(self.saveTime)

        #connect save own data button
        self.pushButton_2.clicked.connect(self.saveMeasuredTime)

        #connect goals button
        self.actualizate_button.clicked.connect(self.actualizateGoalsRedirect)

        #connect graph button
        self.graphs_generate_button.clicked.connect(self.setGraphRedirect)


        #users first time => have to go through registration
        if os.path.exists("data/credential_itu.json"):
            JsonFunctions.SetUserData(self)
            self.stackedWidget.setCurrentWidget(self.profile_widget)
        else:
            self.stackedWidget.setCurrentWidget(self.registration_widget)

        #connect setting buttons
        self.registration_create_button.clicked.connect(self.userRegistration)

        self.save_user_changes_button.clicked.connect(self.userChangeProfile)

        self.pushButton_3.clicked.connect(self.deleteUserProfile)

        self.set_goals_button.clicked.connect(self.setGoals)

        #ensures the movement of the window
        def moveWindow(event):
            if GuiFunctions.returnWindowState(self) == 1:
                self.Maximize()

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        #connect to a mouse event
        self.app_name_frame.mouseMoveEvent = moveWindow

        #connect toggle menu button
        self.toggle_button.clicked.connect(lambda: GuiFunctions.toggleMenu(self))

        #connect set photo button
        self.set_foto_button.clicked.connect(self.browseImage)
        self.show()


    #current mouse position for moveWindow()
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    #saves own goals to a file
    def setGoals(self):
        correct = True
        self.goals_Edit.setStyleSheet(Style.lineEdit)

        if self.goals_Edit.text() == "":
            correct = False
            self.goals_Edit.setStyleSheet(Style.lineEditWrong)

        if not self.goals_Edit.text().isnumeric():
            correct = False
            self.goals_Edit.setStyleSheet(Style.lineEditWrong)

        if correct:
            JsonFunctions.ChangeGoalsData(self, str(self.sports_Box.currentText()), self.goals_Edit.text())
            JsonFunctions.SetUserData(self)
            self.goals_Edit.setText("")

    #print the time
    def time(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        if self.minutes == 60:
            self.minutes = 0
            self.hours +=1


        timeStr = ""
        if self.hours > 0:
            if self.hours < 10:
                timeStr += '0' + str(self.hours) + ':'
            else:
                timeStr += str(self.hours) + ':'

        if self.minutes < 10:
            timeStr += '0' + str(self.minutes) + ':'
        else:
            timeStr += str(self.minutes) + ':'

        if self.seconds < 10:
            timeStr += '0' + str(self.seconds)
        else:
            timeStr += str(self.seconds)

        self.timer_label.setText(timeStr)

    #start timer
    def startTime(self):
        self.timer.start(1000)

    #stop timer
    def stopTime(self):
        self.timer.stop()

    #stop timer and reset time
    def resetTime(self):
        self.timer.stop()
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.timer_label.setText('00:00')

    #stop timer and save the data
    def saveTime(self):
        self.timer.stop()
        if self.minutes == 0:
            if self.seconds != 0:
                JsonFunctions.SaveActivityData(self, str(self.timer_box.currentText()), 1 + (self.hours*60))
        else:
            JsonFunctions.SaveActivityData(self, str(self.timer_box.currentText()), self.minutes + (self.hours*60))

    #save own data
    def saveMeasuredTime(self):
        correct = True
        self.lineEdit.setStyleSheet(Style.lineEdit)

        if self.lineEdit.text() == "":
            correct = False
            self.lineEdit.setStyleSheet(Style.lineEditWrong)

        if not self.lineEdit.text().isnumeric():
            correct = False
            self.lineEdit.setStyleSheet(Style.lineEditWrong)

        if correct:
            JsonFunctions.SaveActivityData(self, str(self.comboBox.currentText()), int(self.lineEdit.text()))
            self.lineEdit.setText("")

    #sets goals to a progress bars
    def actualizateGoalsRedirect(self):
        JsonFunctions.actualizateGoals(self)

    #sets values into a graphs
    def setGraphRedirect(self):
        JsonFunctions.setGraph(self, str(self.graphs_box.currentText()))

    #box to confirm the deletion of the entire profile
    def deleteUserProfile(self):
        box = QtWidgets.QMessageBox()
        box.setStyleSheet(Style.messageBox)
        box.setWindowTitle('Vymazání profilu!')
        box.setText('Opravdu si přejete vymazat profil?')
        box.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        buttonY = box.button(QtWidgets.QMessageBox.Yes)
        buttonY.setText('Ano')
        buttonY.setStyleSheet(Style.messageBoxButton)
        buttonN = box.button(QtWidgets.QMessageBox.No)
        buttonN.setText('Ne')
        buttonN.setStyleSheet(Style.messageBoxButton)
        ret = box.exec_()
        if ret == QtWidgets.QMessageBox.Yes:
            shutil.rmtree("data")
            self.stackedWidget.setCurrentWidget(self.registration_widget)
            self.profile_label.setText("")
            self.run_progressBar.setValue(0)
            self.walk_progressBar.setValue(0)
            self.skate_progressBar.setValue(0)
            self.cycle_progressBar.setValue(0)
            self.week_tab.clear()
            self.month_tab.clear()
            self.year_tab.clear()
            self.registration_name_edit.setText("")
            self.registration_surname_edit.setText("")
            self.registration_height_edit.setText("")
            self.registration_weight_edit.setText("")

    #sets the new user data
    def userChangeProfile(self):
        correct = True
        self.name_edit.setStyleSheet(Style.lineEdit)
        self.surname_edit.setStyleSheet(Style.lineEdit)
        self.height_edit.setStyleSheet(Style.lineEdit)
        self.weight_edit.setStyleSheet(Style.lineEdit)
        name = None
        surname = None
        height = None
        weight = None
        if self.name_edit.text() != "":
            name = self.name_edit.text()
        if self.surname_edit.text() != "":
            surname = self.surname_edit.text()
        if self.height_edit.text() != "":
            height = self.height_edit.text()
        if self.weight_edit.text() != "":
            weight = self.weight_edit.text()

        if not self.height_edit.text().isnumeric():
            correct = False
            self.height_edit.setStyleSheet(Style.lineEditWrong)

        if not self.weight_edit.text().isnumeric():
            correct = False
            self.weight_edit.setStyleSheet(Style.lineEditWrong)

        if correct:
            JsonFunctions.ChangeUserData(self, name, surname, height, weight)
            JsonFunctions.SetUserData(self)

    #new user
    def userRegistration(self):
        correct = True
        self.registration_name_edit.setStyleSheet(Style.lineEdit)
        self.registration_surname_edit.setStyleSheet(Style.lineEdit)
        self.registration_height_edit.setStyleSheet(Style.lineEdit)
        self.registration_weight_edit.setStyleSheet(Style.lineEdit)

        if self.registration_name_edit.text() == "":
            correct = False
            self.registration_name_edit.setStyleSheet(Style.lineEditWrong)
        if self.registration_surname_edit.text() == "":
            correct = False
            self.registration_surname_edit.setStyleSheet(Style.lineEditWrong)
        if self.registration_height_edit.text() == "":
            correct = False
            self.registration_height_edit.setStyleSheet(Style.lineEditWrong)
        if self.registration_weight_edit.text() == "":
            correct = False
            self.registration_weight_edit.setStyleSheet(Style.lineEditWrong)

        if not self.registration_height_edit.text().isnumeric():
            correct = False
            self.registration_height_edit.setStyleSheet(Style.lineEditWrong)

        if not self.registration_weight_edit.text().isnumeric():
            correct = False
            self.registration_weight_edit.setStyleSheet(Style.lineEditWrong)

        if correct:
            self.stackedWidget.setCurrentWidget(self.profile_widget)
            JsonFunctions.SaveUserData(self)
            JsonFunctions.SetUserData(self)


    # change widget and stylesheet when menu button is pressed
    def menuButton(self):
        buttonClicked = self.sender()

        if buttonClicked.objectName() == "profile_button" and self.stackedWidget.currentIndex() != 7:
            self.stackedWidget.setCurrentWidget(self.profile_widget)
            GuiFunctions.SetButtonStyle(self, "profile_button")

        if buttonClicked.objectName() == "timer_button" and self.stackedWidget.currentIndex() != 7:
            self.stackedWidget.setCurrentWidget(self.timer_widget)
            GuiFunctions.SetButtonStyle(self, "timer_button")

        if buttonClicked.objectName() == "settings_button" and self.stackedWidget.currentIndex() != 7:
            self.stackedWidget.setCurrentWidget(self.user_info_widget)
            GuiFunctions.SetButtonStyle(self, "settings_button")

        if buttonClicked.objectName() == "statistics_button" and self.stackedWidget.currentIndex() != 7:
            self.stackedWidget.setCurrentWidget(self.graphs_widget)
            GuiFunctions.SetButtonStyle(self, "statistics_button")

        if buttonClicked.objectName() == "targets_button" and self.stackedWidget.currentIndex() != 7:
            self.stackedWidget.setCurrentWidget(self.goals_overview_widget)
            GuiFunctions.SetButtonStyle(self, "targets_button")

        if buttonClicked.objectName() == "switch_user_button":
            self.stackedWidget.setCurrentWidget(self.goals_info_widget)

        if buttonClicked.objectName() == "switch_goals_button":
            self.stackedWidget.setCurrentWidget(self.user_info_widget)

        if buttonClicked.objectName() == "timer_data_insert_button_2":
            self.stackedWidget.setCurrentWidget(self.insert_data_widget)

        if buttonClicked.objectName() == "pushButton":
            self.stackedWidget.setCurrentWidget(self.timer_widget)

    #Maximize window
    def Maximize(self):
        tmp = GuiFunctions.returnWindowState(self)
        if tmp == 0:
            GuiFunctions.changeWindowState(self, 1)
            self.verticalLayout_17.setContentsMargins(0,0,0,0)
            self.full_screen_button.setIcon(QIcon(QPixmap("icons/shrink.png")))
            self.full_screen_button.setIconSize(QSize(25,25))
            self.showMaximized()
        else:
            GuiFunctions.changeWindowState(self, 0)
            self.verticalLayout_17.setContentsMargins(10, 10, 10, 10)
            self.full_screen_button.setIcon(QIcon(QPixmap("icons/full_screen.png")))
            self.full_screen_button.setIconSize(QSize(25,25))
            self.showNormal()

    # start app at the middle of screen
    def centerOnScreen (self):
        resolution = QDesktopWidget().screenGeometry()
        self.move(round((resolution.width() / 2) - (self.frameSize().width() / 2)),
                  round((resolution.height() / 2) - (self.frameSize().height() / 2)))

    #set image
    def browseImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', './', 'Image files (*.jpg *.png *.jpeg *.gif)')

        imagePath = fname[0]
        self.user_foto_label.setPixmap(QPixmap(imagePath))
        self.profile_foto_label.setPixmap(QPixmap(imagePath))
        JsonFunctions.SaveProfilePicture(self, imagePath)


class LoadingScreen(QtWidgets.QMainWindow, Ui_LoadingScreen):
    def __init__(self, *args, obj=None, **kwargs):
        super(LoadingScreen, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centerOnScreen()

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        #Init timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        #Init Text
        self.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        #Change Texts
        QtCore.QTimer.singleShot(800, lambda: self.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(2000, lambda: self.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        self.show()

    def progress(self):
        global counter
        try:
            if counter == 0:
                pass
        except:
            counter = 0
        #sets value to a progress bar
        self.progressBar.setValue(counter)

        #close loading screen and open app
        if counter > 100:
            #stop timer
            self.timer.stop()

            #show main window
            self.main = MainWindow()
            self.main.centerOnScreen()

            #close loading screen
            self.close()

        #counter inc
        counter += 1

    def centerOnScreen (self):
        resolution = QDesktopWidget().screenGeometry()
        self.move(round((resolution.width() / 2) - (self.frameSize().width() / 2)),
                  round((resolution.height() / 2) - (self.frameSize().height() / 2)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = LoadingScreen()
    app.exec()
