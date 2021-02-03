# Subject: ITU
# School:  Faculty of Information Technology, Brno University of Technology
# Authors: Boris Burkalo
#          Daniel Kamenický
#          Jan Klusáček
#
from ITUsportsTracker import *

#saves state of fullscreen
windowState = 0

class GuiFunctions(MainWindow):

    #sets the upper bar buttons
    def ActivateTopBarButtons(self):
        self.minimalize_button.setIcon(QIcon(QPixmap("icons/minimize.png")))
        self.minimalize_button.setIconSize(QSize(30,30))
        self.minimalize_button.clicked.connect(lambda: self.showMinimized())
        self.full_screen_button.setIcon(QIcon(QPixmap("icons/full_screen.png")))
        self.full_screen_button.setIconSize(QSize(25,25))
        self.full_screen_button.clicked.connect(self.Maximize)
        self.close_button.setIcon(QIcon(QPixmap("icons/close.png")))
        self.close_button.setIconSize(QSize(30,30))
        self.close_button.clicked.connect(lambda: self.close())

    #returns value of current window state
    def returnWindowState(self):
        return windowState

    #change window state
    def changeWindowState(self, number):
        global windowState
        windowState = number

    #sets buttons in menu bar
    def ActivateMenuButtons(self):
        self.profile_button.clicked.connect(self.menuButton)
        self.profile_button.setStyleSheet(Style.buttonStandard)
        self.profile_button.setIcon(QIcon(QPixmap("icons/profile_white.png")))
        self.profile_button.setIconSize(QSize(40,40))
        self.profile_button.setText("     Profil")
        self.timer_button.clicked.connect(self.menuButton)
        self.timer_button.setStyleSheet(Style.buttonStandard)
        self.timer_button.setIcon(QIcon(QPixmap("icons/timer_white.png")))
        self.timer_button.setIconSize(QSize(40,40))
        self.timer_button.setText("     Stopky")
        self.settings_button.clicked.connect(self.menuButton)
        self.settings_button.setStyleSheet(Style.buttonStandard)
        self.settings_button.setIcon(QIcon(QPixmap("icons/settings_white.png")))
        self.settings_button.setIconSize(QSize(40,40))
        self.settings_button.setText("     Nastavení")
        self.statistics_button.clicked.connect(self.menuButton)
        self.statistics_button.setStyleSheet(Style.buttonStandard)
        self.statistics_button.setIcon(QIcon(QPixmap("icons/statistics_white.png")))
        self.statistics_button.setIconSize(QSize(40,40))
        self.statistics_button.setText("     Statistiky")
        self.targets_button.clicked.connect(self.menuButton)
        self.targets_button.setStyleSheet(Style.buttonStandard)
        self.targets_button.setIcon(QIcon(QPixmap("icons/goals_white.png")))
        self.targets_button.setIconSize(QSize(40,40))
        self.targets_button.setText("     Cíle")
        self.switch_user_button.clicked.connect(self.menuButton)
        self.switch_goals_button.clicked.connect(self.menuButton)
        self.timer_data_insert_button_2.clicked.connect(self.menuButton)
        self.pushButton.clicked.connect(self.menuButton)
        self.toggle_button.setStyleSheet(Style.buttonToggle)
        self.toggle_button.setIcon(QIcon(QPixmap("icons/menu.png")))
        self.toggle_button.setIconSize(QSize(40,40))

    #sets design of menu buttons
    def SetButtonStyle(self, name):
        self.timer_button.setStyleSheet(Style.buttonStandard)
        self.timer_button.setIcon(QIcon(QPixmap("icons/timer_white.png")))
        self.timer_button.setIconSize(QSize(40,40))
        self.profile_button.setStyleSheet(Style.buttonStandard)
        self.profile_button.setIcon(QIcon(QPixmap("icons/profile_white.png")))
        self.profile_button.setIconSize(QSize(40,40))
        self.settings_button.setStyleSheet(Style.buttonStandard)
        self.settings_button.setIcon(QIcon(QPixmap("icons/settings_white.png")))
        self.settings_button.setIconSize(QSize(40,40))
        self.statistics_button.setStyleSheet(Style.buttonStandard)
        self.statistics_button.setIcon(QIcon(QPixmap("icons/statistics_white.png")))
        self.statistics_button.setIconSize(QSize(40,40))
        self.targets_button.setStyleSheet(Style.buttonStandard)
        self.targets_button.setIcon(QIcon(QPixmap("icons/goals_white.png")))
        self.targets_button.setIconSize(QSize(40,40))
        if name == "profile_button":
            self.profile_button.setStyleSheet(Style.buttonClicked)
            self.profile_button.setIcon(QIcon(QPixmap("icons/profile_black.png")))
            self.profile_button.setIconSize(QSize(40,40))
        elif name == "timer_button":
            self.timer_button.setStyleSheet(Style.buttonClicked)
            self.timer_button.setIcon(QIcon(QPixmap("icons/timer_black.png")))
            self.timer_button.setIconSize(QSize(40,40))
        elif name == "settings_button":
            self.settings_button.setStyleSheet(Style.buttonClicked)
            self.settings_button.setIcon(QIcon(QPixmap("icons/settings_black.png")))
            self.settings_button.setIconSize(QSize(40,40))
        elif name == "statistics_button":
            self.statistics_button.setStyleSheet(Style.buttonClicked)
            self.statistics_button.setIcon(QIcon(QPixmap("icons/statistics_black.png")))
            self.statistics_button.setIconSize(QSize(40,40))
        elif name == "targets_button":
            self.targets_button.setStyleSheet(Style.buttonClicked)
            self.targets_button.setIcon(QIcon(QPixmap("icons/goals_black.png")))
            self.targets_button.setIconSize(QSize(40,40))

    #handling toggle menu
    def toggleMenu(self):
        width = self.menu_frame.width()
        if width == 70:
            x = 220
        else:
            x = 70
        self.animation = QPropertyAnimation(self.menu_frame, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(x)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
