# Subject: ITU
# School:  Faculty of Information Technology, Brno University of Technology
# Authors: Boris Burkalo
#          Daniel Kamenický
#          Jan Klusáček
#
# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.15.2



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 720))
        MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(27, 29, 35, 160);\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"}")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_17.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setStyleSheet("")
        self.main_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(self.main_frame)
        self.top_frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.top_frame.setStyleSheet("background-color: transparent;\n"
"border: 0px;")
        self.top_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toggle_menu_frame = QtWidgets.QFrame(self.top_frame)
        self.toggle_menu_frame.setMaximumSize(QtCore.QSize(70, 16777215))
        self.toggle_menu_frame.setStyleSheet("border: 0px;")
        self.toggle_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toggle_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toggle_menu_frame.setObjectName("toggle_menu_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.toggle_menu_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toggle_button = QtWidgets.QPushButton(self.toggle_menu_frame)
        self.toggle_button.setEnabled(True)
        self.toggle_button.setMinimumSize(QtCore.QSize(70, 60))
        self.toggle_button.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"}")
        self.toggle_button.setText("")
        self.toggle_button.setObjectName("toggle_button")
        self.verticalLayout_2.addWidget(self.toggle_button)
        self.horizontalLayout_2.addWidget(self.toggle_menu_frame)
        self.top_details_frame = QtWidgets.QFrame(self.top_frame)
        self.top_details_frame.setStyleSheet("background: transparent;\n"
"border: 0px;")
        self.top_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_details_frame.setObjectName("top_details_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.top_details_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.top_buttons_frame = QtWidgets.QFrame(self.top_details_frame)
        self.top_buttons_frame.setMinimumSize(QtCore.QSize(0, 30))
        self.top_buttons_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.top_buttons_frame.setStyleSheet("background-color: rgba(115, 210, 22, 100);\n"
"border:0px;")
        self.top_buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_buttons_frame.setObjectName("top_buttons_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_buttons_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.app_name_frame = QtWidgets.QFrame(self.top_buttons_frame)
        self.app_name_frame.setStyleSheet("")
        self.app_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.app_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.app_name_frame.setObjectName("app_name_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.app_name_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.app_name_label = QtWidgets.QLabel(self.app_name_frame)
        self.app_name_label.setStyleSheet("color: rgb(0,0,0);\n"
"padding-left: 5px;")
        self.app_name_label.setObjectName("app_name_label")
        self.horizontalLayout_5.addWidget(self.app_name_label)
        self.horizontalLayout_3.addWidget(self.app_name_frame)
        self.buttons_frame = QtWidgets.QFrame(self.top_buttons_frame)
        self.buttons_frame.setMaximumSize(QtCore.QSize(120, 16777215))
        self.buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_frame.setObjectName("buttons_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.buttons_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minimalize_button = QtWidgets.QPushButton(self.buttons_frame)
        self.minimalize_button.setMinimumSize(QtCore.QSize(0, 30))
        self.minimalize_button.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(115, 210, 22);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.minimalize_button.setText("")
        self.minimalize_button.setObjectName("minimalize_button")
        self.horizontalLayout_4.addWidget(self.minimalize_button)
        self.full_screen_button = QtWidgets.QPushButton(self.buttons_frame)
        self.full_screen_button.setMinimumSize(QtCore.QSize(0, 30))
        self.full_screen_button.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(115, 210, 22);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.full_screen_button.setText("")
        self.full_screen_button.setObjectName("full_screen_button")
        self.horizontalLayout_4.addWidget(self.full_screen_button)
        self.close_button = QtWidgets.QPushButton(self.buttons_frame)
        self.close_button.setMinimumSize(QtCore.QSize(0, 30))
        self.close_button.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(115, 210, 22);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.close_button.setText("")
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_4.addWidget(self.close_button)
        self.horizontalLayout_3.addWidget(self.buttons_frame)
        self.verticalLayout_3.addWidget(self.top_buttons_frame)
        self.top_info_frame = QtWidgets.QFrame(self.top_details_frame)
        self.top_info_frame.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border: 0px;")
        self.top_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_info_frame.setObjectName("top_info_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.top_info_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.file_path_label = QtWidgets.QLabel(self.top_info_frame)
        self.file_path_label.setStyleSheet("color: rgb(115, 210, 22);\n"
"padding-left: 5px;")
        self.file_path_label.setObjectName("file_path_label")
        self.horizontalLayout_8.addWidget(self.file_path_label)
        self.verticalLayout_3.addWidget(self.top_info_frame)
        self.horizontalLayout_2.addWidget(self.top_details_frame)
        self.verticalLayout.addWidget(self.top_frame)
        self.central_frame = QtWidgets.QFrame(self.main_frame)
        self.central_frame.setStyleSheet("")
        self.central_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.central_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.central_frame.setObjectName("central_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.central_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.menu_frame = QtWidgets.QFrame(self.central_frame)
        self.menu_frame.setMaximumSize(QtCore.QSize(70, 16777215))
        self.menu_frame.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.menu_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.menu_higher_frame = QtWidgets.QFrame(self.menu_frame)
        self.menu_higher_frame.setMaximumSize(QtCore.QSize(16777215, 240))
        self.menu_higher_frame.setStyleSheet("border:none;")
        self.menu_higher_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_higher_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_higher_frame.setObjectName("menu_higher_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.menu_higher_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.profile_button = QtWidgets.QPushButton(self.menu_higher_frame)
        self.profile_button.setMinimumSize(QtCore.QSize(0, 60))
        self.profile_button.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 29, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.profile_button.setText("")
        self.profile_button.setObjectName("profile_button")
        self.verticalLayout_5.addWidget(self.profile_button)
        self.timer_button = QtWidgets.QPushButton(self.menu_higher_frame)
        self.timer_button.setMinimumSize(QtCore.QSize(0, 60))
        self.timer_button.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 29, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.timer_button.setText("")
        self.timer_button.setObjectName("timer_button")
        self.verticalLayout_5.addWidget(self.timer_button)
        self.statistics_button = QtWidgets.QPushButton(self.menu_higher_frame)
        self.statistics_button.setMinimumSize(QtCore.QSize(0, 60))
        self.statistics_button.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 29, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.statistics_button.setText("")
        self.statistics_button.setObjectName("statistics_button")
        self.verticalLayout_5.addWidget(self.statistics_button)
        self.targets_button = QtWidgets.QPushButton(self.menu_higher_frame)
        self.targets_button.setMinimumSize(QtCore.QSize(0, 60))
        self.targets_button.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 29, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.targets_button.setText("")
        self.targets_button.setObjectName("targets_button")
        self.verticalLayout_5.addWidget(self.targets_button)
        self.verticalLayout_4.addWidget(self.menu_higher_frame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.menu_lower_frame = QtWidgets.QFrame(self.menu_frame)
        self.menu_lower_frame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.menu_lower_frame.setStyleSheet("")
        self.menu_lower_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_lower_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_lower_frame.setObjectName("menu_lower_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.menu_lower_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.profile_label = QtWidgets.QLabel(self.menu_lower_frame)
        self.profile_label.setMinimumSize(QtCore.QSize(65, 60))
        self.profile_label.setMaximumSize(QtCore.QSize(60, 60))
        self.profile_label.setStyleSheet("QLabel{\n"
"    color: rgb(115, 210, 22);\n"
"    font: bold 30px;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.profile_label.setText("")
        self.profile_label.setObjectName("profile_label")
        self.verticalLayout_6.addWidget(self.profile_label)
        self.settings_button = QtWidgets.QPushButton(self.menu_lower_frame)
        self.settings_button.setMinimumSize(QtCore.QSize(0, 60))
        self.settings_button.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 29, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.settings_button.setText("")
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout_6.addWidget(self.settings_button)
        self.verticalLayout_4.addWidget(self.menu_lower_frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_6.addWidget(self.menu_frame)
        self.content_frame = QtWidgets.QFrame(self.central_frame)
        self.content_frame.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_frame.setObjectName("content_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.content_frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.central_content_frame = QtWidgets.QFrame(self.content_frame)
        self.central_content_frame.setStyleSheet("")
        self.central_content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.central_content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.central_content_frame.setObjectName("central_content_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.central_content_frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.stackedWidget = QtWidgets.QStackedWidget(self.central_content_frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.user_info_widget = QtWidgets.QWidget()
        self.user_info_widget.setStyleSheet("border: none;")
        self.user_info_widget.setObjectName("user_info_widget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.user_info_widget)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.user_info_frame = QtWidgets.QFrame(self.user_info_widget)
        self.user_info_frame.setMinimumSize(QtCore.QSize(607, 0))
        self.user_info_frame.setMaximumSize(QtCore.QSize(607, 16777215))
        self.user_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_info_frame.setObjectName("user_info_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.user_info_frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.title_user_label = QtWidgets.QLabel(self.user_info_frame)
        self.title_user_label.setMinimumSize(QtCore.QSize(0, 64))
        self.title_user_label.setMaximumSize(QtCore.QSize(16777215, 64))
        self.title_user_label.setStyleSheet("QLabel {\n"
"    font-size: 25px;\n"
"    qproperty-alignment: \'AlignCenter | AlignBottom\';\n"
"}")
        self.title_user_label.setObjectName("title_user_label")
        self.verticalLayout_9.addWidget(self.title_user_label)
        self.name_label = QtWidgets.QLabel(self.user_info_frame)
        self.name_label.setMinimumSize(QtCore.QSize(0, 64))
        self.name_label.setMaximumSize(QtCore.QSize(16777215, 64))
        self.name_label.setStyleSheet("QLabel {\n"
"    qproperty-alignment: \'AlignBottom | AlignLeft\';\n"
"    padding-left: 35px;\n"
"    font-size: 17px;\n"
"}")
        self.name_label.setObjectName("name_label")
        self.verticalLayout_9.addWidget(self.name_label)
        self.name_frame = QtWidgets.QFrame(self.user_info_frame)
        self.name_frame.setMinimumSize(QtCore.QSize(0, 64))
        self.name_frame.setMaximumSize(QtCore.QSize(16777215, 64))
        self.name_frame.setStyleSheet("border: none;")
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.name_frame)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.name_edit = QtWidgets.QLineEdit(self.name_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_edit.sizePolicy().hasHeightForWidth())
        self.name_edit.setSizePolicy(sizePolicy)
        self.name_edit.setMinimumSize(QtCore.QSize(407, 0))
        self.name_edit.setMaximumSize(QtCore.QSize(600, 16777215))
        self.name_edit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.name_edit.setObjectName("name_edit")
        self.horizontalLayout_14.addWidget(self.name_edit)
        spacerItem4 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.verticalLayout_9.addWidget(self.name_frame)
        self.surname_label = QtWidgets.QLabel(self.user_info_frame)
        self.surname_label.setMinimumSize(QtCore.QSize(0, 64))
        self.surname_label.setMaximumSize(QtCore.QSize(16777215, 64))
        self.surname_label.setStyleSheet("QLabel {\n"
"    qproperty-alignment: \'AlignBottom | AlignLeft\';\n"
"    padding-left: 35px;\n"
"    font-size: 17px;\n"
"}")
        self.surname_label.setObjectName("surname_label")
        self.verticalLayout_9.addWidget(self.surname_label)
        self.frame = QtWidgets.QFrame(self.user_info_frame)
        self.frame.setMinimumSize(QtCore.QSize(0, 64))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 64))
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem5)
        self.surname_edit = QtWidgets.QLineEdit(self.frame)
        self.surname_edit.setMinimumSize(QtCore.QSize(407, 0))
        self.surname_edit.setMaximumSize(QtCore.QSize(600, 16777215))
        self.surname_edit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.surname_edit.setObjectName("surname_edit")
        self.horizontalLayout_15.addWidget(self.surname_edit)
        spacerItem6 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem6)
        self.verticalLayout_9.addWidget(self.frame)
        self.height_label = QtWidgets.QLabel(self.user_info_frame)
        self.height_label.setMinimumSize(QtCore.QSize(0, 64))
        self.height_label.setMaximumSize(QtCore.QSize(16777215, 64))
        self.height_label.setStyleSheet("QLabel {\n"
"    qproperty-alignment: \'AlignBottom | AlignLeft\';\n"
"    padding-left: 35px;\n"
"    font-size: 17px;\n"
"}")
        self.height_label.setObjectName("height_label")
        self.verticalLayout_9.addWidget(self.height_label)
        self.frame_2 = QtWidgets.QFrame(self.user_info_frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 64))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 64))
        self.frame_2.setStyleSheet("border: none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem7)
        self.height_edit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height_edit.sizePolicy().hasHeightForWidth())
        self.height_edit.setSizePolicy(sizePolicy)
        self.height_edit.setMinimumSize(QtCore.QSize(407, 0))
        self.height_edit.setMaximumSize(QtCore.QSize(600, 16777215))
        self.height_edit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.height_edit.setObjectName("height_edit")
        self.horizontalLayout_16.addWidget(self.height_edit)
        spacerItem8 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem8)
        self.verticalLayout_9.addWidget(self.frame_2)
        self.weight_label = QtWidgets.QLabel(self.user_info_frame)
        self.weight_label.setMinimumSize(QtCore.QSize(0, 64))
        self.weight_label.setMaximumSize(QtCore.QSize(16777215, 64))
        self.weight_label.setStyleSheet("QLabel {\n"
"    qproperty-alignment: \'AlignBottom | AlignLeft\';\n"
"    padding-left: 35px;\n"
"    font-size: 17px;\n"
"}")
        self.weight_label.setObjectName("weight_label")
        self.verticalLayout_9.addWidget(self.weight_label)
        self.frame_3 = QtWidgets.QFrame(self.user_info_frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 64))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 64))
        self.frame_3.setStyleSheet("border: none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem9)
        self.weight_edit = QtWidgets.QLineEdit(self.frame_3)
        self.weight_edit.setMinimumSize(QtCore.QSize(407, 0))
        self.weight_edit.setMaximumSize(QtCore.QSize(600, 16777215))
        self.weight_edit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.weight_edit.setObjectName("weight_edit")
        self.horizontalLayout_17.addWidget(self.weight_edit)
        spacerItem10 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem10)
        self.verticalLayout_9.addWidget(self.frame_3)
        self.save_changes_frame = QtWidgets.QFrame(self.user_info_frame)
        self.save_changes_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.save_changes_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.save_changes_frame.setStyleSheet("border: 0px;")
        self.save_changes_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.save_changes_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.save_changes_frame.setObjectName("save_changes_frame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.save_changes_frame)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem11 = QtWidgets.QSpacerItem(32, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem11)
        self.pushButton_3 = QtWidgets.QPushButton(self.save_changes_frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 20))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 20))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgba(115, 210, 22, 150);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 0px solid rgba(115, 210, 22, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(115, 210, 22, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 100);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_13.addWidget(self.pushButton_3)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem12)
        self.save_user_changes_button = QtWidgets.QPushButton(self.save_changes_frame)
        self.save_user_changes_button.setMinimumSize(QtCore.QSize(150, 20))
        self.save_user_changes_button.setMaximumSize(QtCore.QSize(150, 20))
        self.save_user_changes_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(115, 210, 22, 150);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 0px solid rgba(115, 210, 22, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(115, 210, 22, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 100);\n"
"}")
        self.save_user_changes_button.setObjectName("save_user_changes_button")
        self.horizontalLayout_13.addWidget(self.save_user_changes_button)
        spacerItem13 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem13)
        self.verticalLayout_9.addWidget(self.save_changes_frame)
        spacerItem14 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem14)
        self.horizontalLayout_10.addWidget(self.user_info_frame)
        self.user_foto_frame = QtWidgets.QFrame(self.user_info_widget)
        self.user_foto_frame.setMinimumSize(QtCore.QSize(300, 0))
        self.user_foto_frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.user_foto_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_foto_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_foto_frame.setObjectName("user_foto_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.user_foto_frame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem15 = QtWidgets.QSpacerItem(20, 128, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem15)
        self.user_photo_frame = QtWidgets.QFrame(self.user_foto_frame)
        self.user_photo_frame.setMaximumSize(QtCore.QSize(16777215, 268))
        self.user_photo_frame.setStyleSheet("border: 0px;")
        self.user_photo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_photo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_photo_frame.setObjectName("user_photo_frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.user_photo_frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.user_foto_label = QtWidgets.QLabel(self.user_photo_frame)
        self.user_foto_label.setMinimumSize(QtCore.QSize(250, 250))
        self.user_foto_label.setMaximumSize(QtCore.QSize(250, 250))
        self.user_foto_label.setStyleSheet("QLabel {\n"
"    font-size: 25px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    border: 1px solid rgb(115, 210, 22);\n"
"}")
        self.user_foto_label.setScaledContents(True)
        self.user_foto_label.setObjectName("user_foto_label")
        self.horizontalLayout_11.addWidget(self.user_foto_label)
        self.verticalLayout_8.addWidget(self.user_photo_frame)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem16)
        self.set_foto_frame = QtWidgets.QFrame(self.user_foto_frame)
        self.set_foto_frame.setMaximumSize(QtCore.QSize(16777215, 38))
        self.set_foto_frame.setStyleSheet("border: 0px;")
        self.set_foto_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.set_foto_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.set_foto_frame.setObjectName("set_foto_frame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.set_foto_frame)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.set_foto_button = QtWidgets.QPushButton(self.set_foto_frame)
        self.set_foto_button.setMinimumSize(QtCore.QSize(250, 20))
        self.set_foto_button.setMaximumSize(QtCore.QSize(250, 20))
        self.set_foto_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(115, 210, 22, 150);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 0px solid rgba(115, 210, 22, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(115, 210, 22, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 100);\n"
"}")
        self.set_foto_button.setObjectName("set_foto_button")
        self.horizontalLayout_12.addWidget(self.set_foto_button)
        self.verticalLayout_8.addWidget(self.set_foto_frame)
        spacerItem17 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem17)
        self.switch_setting_frame = QtWidgets.QFrame(self.user_foto_frame)
        self.switch_setting_frame.setMinimumSize(QtCore.QSize(0, 38))
        self.switch_setting_frame.setMaximumSize(QtCore.QSize(16777215, 38))
        self.switch_setting_frame.setStyleSheet("border: none;")
        self.switch_setting_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.switch_setting_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.switch_setting_frame.setObjectName("switch_setting_frame")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.switch_setting_frame)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem18 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem18)
        self.switch_user_button = QtWidgets.QPushButton(self.switch_setting_frame)
        self.switch_user_button.setMinimumSize(QtCore.QSize(124, 20))
        self.switch_user_button.setMaximumSize(QtCore.QSize(124, 20))
        self.switch_user_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(115, 210, 22, 150);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 0px solid rgba(115, 210, 22, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(115, 210, 22, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 100);\n"
"}")
        self.switch_user_button.setObjectName("switch_user_button")
        self.horizontalLayout_18.addWidget(self.switch_user_button)
        self.verticalLayout_8.addWidget(self.switch_setting_frame)
        spacerItem19 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem19)
        self.horizontalLayout_10.addWidget(self.user_foto_frame)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem20)
        self.stackedWidget.addWidget(self.user_info_widget)
        self.goals_info_widget = QtWidgets.QWidget()
        self.goals_info_widget.setAutoFillBackground(False)
        self.goals_info_widget.setStyleSheet("border: none;")
        self.goals_info_widget.setObjectName("goals_info_widget")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.goals_info_widget)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem21)
        self.goals_info_frame = QtWidgets.QFrame(self.goals_info_widget)
        self.goals_info_frame.setMinimumSize(QtCore.QSize(907, 0))
        self.goals_info_frame.setMaximumSize(QtCore.QSize(907, 16777215))
        self.goals_info_frame.setStyleSheet("")
        self.goals_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.goals_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.goals_info_frame.setObjectName("goals_info_frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.goals_info_frame)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.goals_info_frame)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setStyleSheet("QLabel {\n"
"    font-size: 30px;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.goals_info_frame)
        self.label_2.setMinimumSize(QtCore.QSize(0, 72))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 72))
        self.label_2.setStyleSheet("QLabel {\n"
"    font-size: 16px;\n"
"    qproperty-alignment: AlignBottom;\n"
"    padding-left: 10px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(self.label_2)
        self.goals_box_frame = QtWidgets.QFrame(self.goals_info_frame)
        self.goals_box_frame.setMinimumSize(QtCore.QSize(0, 72))
        self.goals_box_frame.setMaximumSize(QtCore.QSize(16777215, 72))
        self.goals_box_frame.setStyleSheet("border: none;")
        self.goals_box_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.goals_box_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.goals_box_frame.setObjectName("goals_box_frame")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.goals_box_frame)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem22)
        self.sports_Box = QtWidgets.QComboBox(self.goals_box_frame)
        self.sports_Box.setMinimumSize(QtCore.QSize(200, 0))
        self.sports_Box.setAcceptDrops(False)
        self.sports_Box.setStyleSheet("QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"}")
        self.sports_Box.setModelColumn(0)
        self.sports_Box.setObjectName("sports_Box")
        self.sports_Box.addItem("")
        self.sports_Box.addItem("")
        self.sports_Box.addItem("")
        self.sports_Box.addItem("")
        self.horizontalLayout_22.addWidget(self.sports_Box)
        spacerItem23 = QtWidgets.QSpacerItem(638, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem23)
        self.verticalLayout_10.addWidget(self.goals_box_frame)
        self.set_goals_frame = QtWidgets.QFrame(self.goals_info_frame)
        self.set_goals_frame.setMinimumSize(QtCore.QSize(0, 72))
        self.set_goals_frame.setMaximumSize(QtCore.QSize(16777215, 72))
        self.set_goals_frame.setStyleSheet("border: none;")
        self.set_goals_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.set_goals_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.set_goals_frame.setObjectName("set_goals_frame")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.set_goals_frame)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem24)
        self.goals_Edit = QtWidgets.QLineEdit(self.set_goals_frame)
        self.goals_Edit.setMinimumSize(QtCore.QSize(407, 0))
        self.goals_Edit.setMaximumSize(QtCore.QSize(600, 16777215))
        self.goals_Edit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.goals_Edit.setObjectName("goals_Edit")
        self.horizontalLayout_21.addWidget(self.goals_Edit)
        self.set_goals_button = QtWidgets.QPushButton(self.set_goals_frame)
        self.set_goals_button.setMinimumSize(QtCore.QSize(100, 20))
        self.set_goals_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(115, 210, 22, 150);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 0px solid rgba(115, 210, 22, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(115, 210, 22, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 100);\n"
"}")
        self.set_goals_button.setObjectName("set_goals_button")
        self.horizontalLayout_21.addWidget(self.set_goals_button)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem25)
        self.verticalLayout_10.addWidget(self.set_goals_frame)
        self.goals_switch_frame = QtWidgets.QFrame(self.goals_info_frame)
        self.goals_switch_frame.setMaximumSize(QtCore.QSize(16777215, 300))
        self.goals_switch_frame.setStyleSheet("border: none;")
        self.goals_switch_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.goals_switch_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.goals_switch_frame.setObjectName("goals_switch_frame")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.goals_switch_frame)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem26)
        self.switch_button_frame = QtWidgets.QFrame(self.goals_switch_frame)
        self.switch_button_frame.setStyleSheet("border: none;")
        self.switch_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.switch_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.switch_button_frame.setObjectName("switch_button_frame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.switch_button_frame)
        self.verticalLayout_11.setContentsMargins(0, 0, 11, 9)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem27 = QtWidgets.QSpacerItem(20, 267, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem27)
        self.switch_goals_button = QtWidgets.QPushButton(self.switch_button_frame)
        self.switch_goals_button.setMinimumSize(QtCore.QSize(124, 20))
        self.switch_goals_button.setMaximumSize(QtCore.QSize(124, 20))
        self.switch_goals_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(115, 210, 22, 150);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 0px solid rgba(115, 210, 22, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(115, 210, 22, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 100);\n"
"}")
        self.switch_goals_button.setObjectName("switch_goals_button")
        self.verticalLayout_11.addWidget(self.switch_goals_button)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem28)
        self.horizontalLayout_20.addWidget(self.switch_button_frame)
        self.verticalLayout_10.addWidget(self.goals_switch_frame)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem29)
        self.horizontalLayout_19.addWidget(self.goals_info_frame)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem30)
        self.stackedWidget.addWidget(self.goals_info_widget)
        self.profile_widget = QtWidgets.QWidget()
        self.profile_widget.setObjectName("profile_widget")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.profile_widget)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.profile_frame = QtWidgets.QFrame(self.profile_widget)
        self.profile_frame.setStyleSheet("border: none;")
        self.profile_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_frame.setObjectName("profile_frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.profile_frame)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.profile_foto_frame = QtWidgets.QFrame(self.profile_frame)
        self.profile_foto_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_foto_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_foto_frame.setObjectName("profile_foto_frame")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.profile_foto_frame)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem31)
        self.profile_foto_label = QtWidgets.QLabel(self.profile_foto_frame)
        self.profile_foto_label.setMinimumSize(QtCore.QSize(250, 250))
        self.profile_foto_label.setMaximumSize(QtCore.QSize(250, 250))
        self.profile_foto_label.setStyleSheet("QLabel {\n"
"    font-size: 25px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    border: 1px solid rgb(115, 210, 22);\n"
"}")
        self.profile_foto_label.setScaledContents(True)
        self.profile_foto_label.setObjectName("profile_foto_label")
        self.horizontalLayout_29.addWidget(self.profile_foto_label)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem32)
        self.verticalLayout_12.addWidget(self.profile_foto_frame)
        self.profile_info_frame = QtWidgets.QFrame(self.profile_frame)
        self.profile_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_info_frame.setObjectName("profile_info_frame")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.profile_info_frame)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.profile_details_frame = QtWidgets.QFrame(self.profile_info_frame)
        self.profile_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_details_frame.setObjectName("profile_details_frame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.profile_details_frame)
        self.verticalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.profile_name_frame = QtWidgets.QFrame(self.profile_details_frame)
        self.profile_name_frame.setMinimumSize(QtCore.QSize(0, 68))
        self.profile_name_frame.setMaximumSize(QtCore.QSize(16777215, 68))
        self.profile_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_name_frame.setObjectName("profile_name_frame")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.profile_name_frame)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        spacerItem33 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem33)
        self.label_4 = QtWidgets.QLabel(self.profile_name_frame)
        self.label_4.setMinimumSize(QtCore.QSize(180, 0))
        self.label_4.setMaximumSize(QtCore.QSize(220, 16777215))
        self.label_4.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    padding-right: 2px;\n"
"    qproperty-alignment: \'AlignRight | AlignVCenter\' ;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_30.addWidget(self.label_4)
        self.edit_name_frame = QtWidgets.QFrame(self.profile_name_frame)
        self.edit_name_frame.setMinimumSize(QtCore.QSize(210, 0))
        self.edit_name_frame.setMaximumSize(QtCore.QSize(210, 16777215))
        self.edit_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_name_frame.setObjectName("edit_name_frame")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.edit_name_frame)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.profile_name_label = QtWidgets.QLabel(self.edit_name_frame)
        self.profile_name_label.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    padding-left: 10px;\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.profile_name_label.setText("")
        self.profile_name_label.setObjectName("profile_name_label")
        self.horizontalLayout_38.addWidget(self.profile_name_label)
        self.horizontalLayout_30.addWidget(self.edit_name_frame)
        self.verticalLayout_13.addWidget(self.profile_name_frame)
        self.profile_surname_frame = QtWidgets.QFrame(self.profile_details_frame)
        self.profile_surname_frame.setMinimumSize(QtCore.QSize(0, 68))
        self.profile_surname_frame.setMaximumSize(QtCore.QSize(16777215, 68))
        self.profile_surname_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_surname_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_surname_frame.setObjectName("profile_surname_frame")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.profile_surname_frame)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        spacerItem34 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem34)
        self.label_5 = QtWidgets.QLabel(self.profile_surname_frame)
        self.label_5.setMinimumSize(QtCore.QSize(180, 0))
        self.label_5.setMaximumSize(QtCore.QSize(220, 16777215))
        self.label_5.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    padding-right: 2px;\n"
"    qproperty-alignment: \'AlignRight | AlignVCenter\' ;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_31.addWidget(self.label_5)
        self.edit_surname_frame = QtWidgets.QFrame(self.profile_surname_frame)
        self.edit_surname_frame.setMinimumSize(QtCore.QSize(210, 0))
        self.edit_surname_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_surname_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_surname_frame.setObjectName("edit_surname_frame")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.edit_surname_frame)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.profile_surname_label = QtWidgets.QLabel(self.edit_surname_frame)
        self.profile_surname_label.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    padding-left: 10px;\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.profile_surname_label.setText("")
        self.profile_surname_label.setObjectName("profile_surname_label")
        self.horizontalLayout_39.addWidget(self.profile_surname_label)
        self.horizontalLayout_31.addWidget(self.edit_surname_frame)
        self.verticalLayout_13.addWidget(self.profile_surname_frame)
        self.profile_height_frame = QtWidgets.QFrame(self.profile_details_frame)
        self.profile_height_frame.setMinimumSize(QtCore.QSize(0, 68))
        self.profile_height_frame.setMaximumSize(QtCore.QSize(16777215, 68))
        self.profile_height_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_height_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_height_frame.setObjectName("profile_height_frame")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.profile_height_frame)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        spacerItem35 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem35)
        self.label_6 = QtWidgets.QLabel(self.profile_height_frame)
        self.label_6.setMinimumSize(QtCore.QSize(180, 0))
        self.label_6.setMaximumSize(QtCore.QSize(220, 16777215))
        self.label_6.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    padding-right: 2px;\n"
"    qproperty-alignment: \'AlignRight | AlignVCenter\' ;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_32.addWidget(self.label_6)
        self.edit_height_frame = QtWidgets.QFrame(self.profile_height_frame)
        self.edit_height_frame.setMinimumSize(QtCore.QSize(210, 0))
        self.edit_height_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_height_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_height_frame.setObjectName("edit_height_frame")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.edit_height_frame)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.profile_height_label = QtWidgets.QLabel(self.edit_height_frame)
        self.profile_height_label.setMaximumSize(QtCore.QSize(55, 16777215))
        self.profile_height_label.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    padding-left: 10px;\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.profile_height_label.setText("")
        self.profile_height_label.setObjectName("profile_height_label")
        self.horizontalLayout_40.addWidget(self.profile_height_label)
        self.label_32 = QtWidgets.QLabel(self.edit_height_frame)
        self.label_32.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_40.addWidget(self.label_32)
        self.horizontalLayout_32.addWidget(self.edit_height_frame)
        self.verticalLayout_13.addWidget(self.profile_height_frame)
        self.profile_weight_frame = QtWidgets.QFrame(self.profile_details_frame)
        self.profile_weight_frame.setMinimumSize(QtCore.QSize(0, 68))
        self.profile_weight_frame.setMaximumSize(QtCore.QSize(16777215, 68))
        self.profile_weight_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_weight_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_weight_frame.setObjectName("profile_weight_frame")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.profile_weight_frame)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        spacerItem36 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem36)
        self.label_7 = QtWidgets.QLabel(self.profile_weight_frame)
        self.label_7.setMinimumSize(QtCore.QSize(180, 0))
        self.label_7.setMaximumSize(QtCore.QSize(220, 16777215))
        self.label_7.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    padding-right: 2px;\n"
"    qproperty-alignment: \'AlignRight | AlignVCenter\' ;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_33.addWidget(self.label_7)
        self.edit_weight_frame = QtWidgets.QFrame(self.profile_weight_frame)
        self.edit_weight_frame.setMinimumSize(QtCore.QSize(210, 0))
        self.edit_weight_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_weight_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_weight_frame.setObjectName("edit_weight_frame")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.edit_weight_frame)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.profile_weight_label = QtWidgets.QLabel(self.edit_weight_frame)
        self.profile_weight_label.setMaximumSize(QtCore.QSize(55, 16777215))
        self.profile_weight_label.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    padding-left: 10px;\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.profile_weight_label.setText("")
        self.profile_weight_label.setObjectName("profile_weight_label")
        self.horizontalLayout_41.addWidget(self.profile_weight_label)
        self.label_33 = QtWidgets.QLabel(self.edit_weight_frame)
        self.label_33.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_41.addWidget(self.label_33)
        self.horizontalLayout_33.addWidget(self.edit_weight_frame)
        self.verticalLayout_13.addWidget(self.profile_weight_frame)
        spacerItem37 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem37)
        self.horizontalLayout_28.addWidget(self.profile_details_frame)
        self.profile_goals_frame = QtWidgets.QFrame(self.profile_info_frame)
        self.profile_goals_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_goals_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_goals_frame.setObjectName("profile_goals_frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.profile_goals_frame)
        self.verticalLayout_14.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_14 = QtWidgets.QFrame(self.profile_goals_frame)
        self.frame_14.setMinimumSize(QtCore.QSize(0, 68))
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 68))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_12 = QtWidgets.QLabel(self.frame_14)
        self.label_12.setMinimumSize(QtCore.QSize(110, 0))
        self.label_12.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_12.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    padding-right: 2px;\n"
"    qproperty-alignment: \'AlignRight | AlignVCenter\' ;\n"
"}")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_34.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.frame_14)
        self.label_13.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    padding-left: 10px;\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_34.addWidget(self.label_13)
        self.label_22 = QtWidgets.QLabel(self.frame_14)
        self.label_22.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_34.addWidget(self.label_22)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem38)
        self.verticalLayout_14.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.profile_goals_frame)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 68))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 68))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_14 = QtWidgets.QLabel(self.frame_15)
        self.label_14.setMinimumSize(QtCore.QSize(110, 0))
        self.label_14.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_14.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    padding-right: 2px;\n"
"    qproperty-alignment: \'AlignRight | AlignVCenter\' ;\n"
"}")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_35.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.frame_15)
        self.label_15.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    padding-left: 10px;\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_35.addWidget(self.label_15)
        self.label_29 = QtWidgets.QLabel(self.frame_15)
        self.label_29.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_35.addWidget(self.label_29)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem39)
        self.verticalLayout_14.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.profile_goals_frame)
        self.frame_16.setMinimumSize(QtCore.QSize(0, 68))
        self.frame_16.setMaximumSize(QtCore.QSize(16777215, 68))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_16 = QtWidgets.QLabel(self.frame_16)
        self.label_16.setMinimumSize(QtCore.QSize(110, 0))
        self.label_16.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_16.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    padding-right: 2px;\n"
"    qproperty-alignment: \'AlignRight | AlignVCenter\' ;\n"
"}")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_36.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.frame_16)
        self.label_17.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    padding-left: 10px;\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_36.addWidget(self.label_17)
        self.label_30 = QtWidgets.QLabel(self.frame_16)
        self.label_30.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_36.addWidget(self.label_30)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem40)
        self.verticalLayout_14.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.profile_goals_frame)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 68))
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 68))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_18 = QtWidgets.QLabel(self.frame_17)
        self.label_18.setMinimumSize(QtCore.QSize(110, 0))
        self.label_18.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_18.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    padding-right: 2px;\n"
"    qproperty-alignment: \'AlignRight | AlignVCenter\' ;\n"
"}")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_37.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.frame_17)
        self.label_19.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    padding-left: 10px;\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_37.addWidget(self.label_19)
        self.label_31 = QtWidgets.QLabel(self.frame_17)
        self.label_31.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: \'AlignLeft | AlignVCenter\';\n"
"    color: rgb(115, 210, 22)\n"
"}")
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_37.addWidget(self.label_31)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem41)
        self.verticalLayout_14.addWidget(self.frame_17)
        spacerItem42 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem42)
        self.horizontalLayout_28.addWidget(self.profile_goals_frame)
        self.verticalLayout_12.addWidget(self.profile_info_frame)
        self.horizontalLayout_23.addWidget(self.profile_frame)
        self.stackedWidget.addWidget(self.profile_widget)
        self.timer_widget = QtWidgets.QWidget()
        self.timer_widget.setStyleSheet("")
        self.timer_widget.setObjectName("timer_widget")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.timer_widget)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.timer_frame = QtWidgets.QFrame(self.timer_widget)
        self.timer_frame.setStyleSheet("border: none;")
        self.timer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timer_frame.setObjectName("timer_frame")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.timer_frame)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem43 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_15.addItem(spacerItem43)
        self.timer_data_frame = QtWidgets.QFrame(self.timer_frame)
        self.timer_data_frame.setMinimumSize(QtCore.QSize(0, 150))
        self.timer_data_frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.timer_data_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timer_data_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timer_data_frame.setObjectName("timer_data_frame")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.timer_data_frame)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.timer_label = QtWidgets.QLabel(self.timer_data_frame)
        self.timer_label.setMaximumSize(QtCore.QSize(250, 100))
        self.timer_label.setStyleSheet("QLabel {\n"
"    font-size: 50px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    border: 5px solid rgb(27, 29, 35);\n"
"    border-radius: 20px;\n"
"    color: rgb(115, 210, 22);\n"
"}")
        self.timer_label.setObjectName("timer_label")
        self.horizontalLayout_43.addWidget(self.timer_label)
        self.verticalLayout_15.addWidget(self.timer_data_frame)
        self.timer_box_frame = QtWidgets.QFrame(self.timer_frame)
        self.timer_box_frame.setMinimumSize(QtCore.QSize(0, 100))
        self.timer_box_frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.timer_box_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timer_box_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timer_box_frame.setObjectName("timer_box_frame")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.timer_box_frame)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.timer_box = QtWidgets.QComboBox(self.timer_box_frame)
        self.timer_box.setMaximumSize(QtCore.QSize(200, 16777215))
        self.timer_box.setStyleSheet("QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"}")
        self.timer_box.setObjectName("timer_box")
        self.timer_box.addItem("")
        self.timer_box.addItem("")
        self.timer_box.addItem("")
        self.timer_box.addItem("")
        self.horizontalLayout_42.addWidget(self.timer_box)
        self.verticalLayout_15.addWidget(self.timer_box_frame)
        self.timer_buttons_frame = QtWidgets.QFrame(self.timer_frame)
        self.timer_buttons_frame.setMinimumSize(QtCore.QSize(0, 150))
        self.timer_buttons_frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.timer_buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timer_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timer_buttons_frame.setObjectName("timer_buttons_frame")
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout(self.timer_buttons_frame)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem44)
        self.timer_start_button = QtWidgets.QPushButton(self.timer_buttons_frame)
        self.timer_start_button.setMinimumSize(QtCore.QSize(100, 100))
        self.timer_start_button.setMaximumSize(QtCore.QSize(100, 100))
        self.timer_start_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"    color: rgb(136, 138, 133);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 29, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(115, 210, 22,100);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.timer_start_button.setObjectName("timer_start_button")
        self.horizontalLayout_44.addWidget(self.timer_start_button)
        spacerItem45 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem45)
        self.timer_stop_button = QtWidgets.QPushButton(self.timer_buttons_frame)
        self.timer_stop_button.setMinimumSize(QtCore.QSize(100, 100))
        self.timer_stop_button.setMaximumSize(QtCore.QSize(100, 100))
        self.timer_stop_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"    color: rgb(136, 138, 133);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 29, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(115, 210, 22,100);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.timer_stop_button.setObjectName("timer_stop_button")
        self.horizontalLayout_44.addWidget(self.timer_stop_button)
        spacerItem46 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem46)
        self.timer_reset_button = QtWidgets.QPushButton(self.timer_buttons_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer_reset_button.sizePolicy().hasHeightForWidth())
        self.timer_reset_button.setSizePolicy(sizePolicy)
        self.timer_reset_button.setMinimumSize(QtCore.QSize(100, 100))
        self.timer_reset_button.setMaximumSize(QtCore.QSize(100, 100))
        self.timer_reset_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"    color: rgb(136, 138, 133);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 29, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(115, 210, 22,100);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.timer_reset_button.setObjectName("timer_reset_button")
        self.horizontalLayout_44.addWidget(self.timer_reset_button)
        spacerItem47 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem47)
        self.timer_save_button = QtWidgets.QPushButton(self.timer_buttons_frame)
        self.timer_save_button.setMinimumSize(QtCore.QSize(100, 100))
        self.timer_save_button.setMaximumSize(QtCore.QSize(100, 100))
        self.timer_save_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"    color: rgb(136, 138, 133);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 29, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(115, 210, 22,100);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.timer_save_button.setObjectName("timer_save_button")
        self.horizontalLayout_44.addWidget(self.timer_save_button)
        spacerItem48 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem48)
        self.verticalLayout_15.addWidget(self.timer_buttons_frame)
        self.timer_switch_button_frame = QtWidgets.QFrame(self.timer_frame)
        self.timer_switch_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timer_switch_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timer_switch_button_frame.setObjectName("timer_switch_button_frame")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.timer_switch_button_frame)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        spacerItem49 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_45.addItem(spacerItem49)
        spacerItem50 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_45.addItem(spacerItem50)
        self.timer_data_insert_button_2 = QtWidgets.QPushButton(self.timer_switch_button_frame)
        self.timer_data_insert_button_2.setMinimumSize(QtCore.QSize(200, 20))
        self.timer_data_insert_button_2.setMaximumSize(QtCore.QSize(200, 20))
        self.timer_data_insert_button_2.setStyleSheet("QPushButton {\n"
"    background-color: rgba(115, 210, 22, 150);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 0px solid rgba(115, 210, 22, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(115, 210, 22, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 100);\n"
"}")
        self.timer_data_insert_button_2.setObjectName("timer_data_insert_button_2")
        self.horizontalLayout_45.addWidget(self.timer_data_insert_button_2)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_45.addItem(spacerItem51)
        self.verticalLayout_15.addWidget(self.timer_switch_button_frame)
        spacerItem52 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem52)
        self.horizontalLayout_24.addWidget(self.timer_frame)
        self.stackedWidget.addWidget(self.timer_widget)
        self.insert_data_widget = QtWidgets.QWidget()
        self.insert_data_widget.setObjectName("insert_data_widget")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.insert_data_widget)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.frame_6 = QtWidgets.QFrame(self.insert_data_widget)
        self.frame_6.setStyleSheet("border:none;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_4 = QtWidgets.QFrame(self.frame_6)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMinimumSize(QtCore.QSize(0, 100))
        self.label_3.setStyleSheet("QLabel {\n"
"    font-size: 30px;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_48.addWidget(self.label_3)
        self.verticalLayout_16.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox.setStyleSheet("QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_47.addWidget(self.comboBox)
        self.verticalLayout_16.addWidget(self.frame_5)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_46.addItem(spacerItem53)
        self.label_9 = QtWidgets.QLabel(self.frame_9)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_46.addWidget(self.label_9)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_46.addWidget(self.lineEdit)
        spacerItem54 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_46.addItem(spacerItem54)
        self.verticalLayout_16.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"    color: rgb(136, 138, 133);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 29, 35);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(115, 210, 22,100);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_49.addWidget(self.pushButton_2)
        self.verticalLayout_16.addWidget(self.frame_10)
        spacerItem55 = QtWidgets.QSpacerItem(20, 96, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_16.addItem(spacerItem55)
        self.frame_11 = QtWidgets.QFrame(self.frame_6)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        spacerItem56 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_50.addItem(spacerItem56)
        spacerItem57 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_50.addItem(spacerItem57)
        self.pushButton = QtWidgets.QPushButton(self.frame_11)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 20))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 20))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(115, 210, 22, 150);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 0px solid rgba(115, 210, 22, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(115, 210, 22, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 100);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_50.addWidget(self.pushButton)
        spacerItem58 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_50.addItem(spacerItem58)
        self.verticalLayout_16.addWidget(self.frame_11)
        spacerItem59 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem59)
        self.horizontalLayout_25.addWidget(self.frame_6)
        self.stackedWidget.addWidget(self.insert_data_widget)
        self.graphs_widget = QtWidgets.QWidget()
        self.graphs_widget.setObjectName("graphs_widget")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.graphs_widget)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.graphs_frame = QtWidgets.QFrame(self.graphs_widget)
        self.graphs_frame.setStyleSheet("border: none;")
        self.graphs_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphs_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphs_frame.setObjectName("graphs_frame")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.graphs_frame)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.tabWidget = QtWidgets.QTabWidget(self.graphs_frame)
        self.tabWidget.setStyleSheet("QTabWidget {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.week_tab = PlotWidget()
        self.week_tab.setObjectName("week_tab")
        self.tabWidget.addTab(self.week_tab, "")
        self.month_tab = PlotWidget()
        self.month_tab.setObjectName("month_tab")
        self.tabWidget.addTab(self.month_tab, "")
        self.year_tab = PlotWidget()
        self.year_tab.setObjectName("year_tab")
        self.tabWidget.addTab(self.year_tab, "")
        self.verticalLayout_18.addWidget(self.tabWidget)
        self.graphs_menu_frame = QtWidgets.QFrame(self.graphs_frame)
        self.graphs_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphs_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphs_menu_frame.setObjectName("graphs_menu_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.graphs_menu_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem60 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem60)
        self.graphs_box = QtWidgets.QComboBox(self.graphs_menu_frame)
        self.graphs_box.setMinimumSize(QtCore.QSize(150, 0))
        self.graphs_box.setMaximumSize(QtCore.QSize(150, 16777215))
        self.graphs_box.setStyleSheet("QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"}")
        self.graphs_box.setObjectName("graphs_box")
        self.graphs_box.addItem("")
        self.graphs_box.addItem("")
        self.graphs_box.addItem("")
        self.graphs_box.addItem("")
        self.horizontalLayout.addWidget(self.graphs_box)
        self.graphs_generate_button = QtWidgets.QPushButton(self.graphs_menu_frame)
        self.graphs_generate_button.setMinimumSize(QtCore.QSize(150, 20))
        self.graphs_generate_button.setMaximumSize(QtCore.QSize(150, 20))
        self.graphs_generate_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(115, 210, 22, 150);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 0px solid rgba(115, 210, 22, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(115, 210, 22, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 100);\n"
"}")
        self.graphs_generate_button.setObjectName("graphs_generate_button")
        self.horizontalLayout.addWidget(self.graphs_generate_button)
        spacerItem61 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem61)
        self.verticalLayout_18.addWidget(self.graphs_menu_frame)
        self.horizontalLayout_26.addWidget(self.graphs_frame)
        self.stackedWidget.addWidget(self.graphs_widget)
        self.goals_overview_widget = QtWidgets.QWidget()
        self.goals_overview_widget.setObjectName("goals_overview_widget")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.goals_overview_widget)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.goals_overview_frame = QtWidgets.QFrame(self.goals_overview_widget)
        self.goals_overview_frame.setStyleSheet("border:none;")
        self.goals_overview_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.goals_overview_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.goals_overview_frame.setObjectName("goals_overview_frame")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.goals_overview_frame)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_8 = QtWidgets.QLabel(self.goals_overview_frame)
        self.label_8.setMinimumSize(QtCore.QSize(0, 80))
        self.label_8.setStyleSheet("QLabel {\n"
"    font-size: 30px;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_19.addWidget(self.label_8)
        spacerItem62 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_19.addItem(spacerItem62)
        self.run_frame = QtWidgets.QFrame(self.goals_overview_frame)
        self.run_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.run_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.run_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.run_frame.setObjectName("run_frame")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.run_frame)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.label_10 = QtWidgets.QLabel(self.run_frame)
        self.label_10.setStyleSheet("QLabel {\n"
"    padding-left: 45px;\n"
"    font-size: 18px;\n"
"    padding-right: 5px;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_51.addWidget(self.label_10)
        self.run_progressBar = QtWidgets.QProgressBar(self.run_frame)
        self.run_progressBar.setStyleSheet("QProgressBar {\n"
"\n"
"    background-color: rgb(44, 49, 60);\n"
"    color: rgb(0,0,0);\n"
"    border: 1px solid rgb(28, 27, 27);\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(115, 210, 22, 255), stop:1 rgba(21, 92, 13, 255));\n"
"}")
        self.run_progressBar.setProperty("value", 0)
        self.run_progressBar.setObjectName("run_progressBar")
        self.horizontalLayout_51.addWidget(self.run_progressBar)
        spacerItem63 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_51.addItem(spacerItem63)
        self.verticalLayout_19.addWidget(self.run_frame)
        self.walk_frame = QtWidgets.QFrame(self.goals_overview_frame)
        self.walk_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.walk_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.walk_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.walk_frame.setObjectName("walk_frame")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.walk_frame)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.label_20 = QtWidgets.QLabel(self.walk_frame)
        self.label_20.setStyleSheet("QLabel {\n"
"    padding-left: 27px;\n"
"    font-size: 18px;\n"
"    padding-right: 5px;\n"
"}")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_53.addWidget(self.label_20)
        self.walk_progressBar = QtWidgets.QProgressBar(self.walk_frame)
        self.walk_progressBar.setStyleSheet("QProgressBar {\n"
"\n"
"    background-color: rgb(44, 49, 60);\n"
"    color: rgb(0,0,0);\n"
"    border: 1px solid rgb(28, 27, 27);\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(115, 210, 22, 255), stop:1 rgba(21, 92, 13, 255));\n"
"}")
        self.walk_progressBar.setProperty("value", 0)
        self.walk_progressBar.setObjectName("walk_progressBar")
        self.horizontalLayout_53.addWidget(self.walk_progressBar)
        spacerItem64 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_53.addItem(spacerItem64)
        self.verticalLayout_19.addWidget(self.walk_frame)
        self.skate_frame = QtWidgets.QFrame(self.goals_overview_frame)
        self.skate_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.skate_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.skate_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.skate_frame.setObjectName("skate_frame")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout(self.skate_frame)
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.label_11 = QtWidgets.QLabel(self.skate_frame)
        self.label_11.setStyleSheet("QLabel {\n"
"    padding-left: 10px;\n"
"    font-size: 18px;\n"
"    padding-right: 5px;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_52.addWidget(self.label_11)
        self.skate_progressBar = QtWidgets.QProgressBar(self.skate_frame)
        self.skate_progressBar.setStyleSheet("QProgressBar {\n"
"\n"
"    background-color: rgb(44, 49, 60);\n"
"    color: rgb(0,0,0);\n"
"    border: 1px solid rgb(28, 27, 27);\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(115, 210, 22, 255), stop:1 rgba(21, 92, 13, 255));\n"
"}")
        self.skate_progressBar.setProperty("value", 0)
        self.skate_progressBar.setObjectName("skate_progressBar")
        self.horizontalLayout_52.addWidget(self.skate_progressBar)
        spacerItem65 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_52.addItem(spacerItem65)
        self.verticalLayout_19.addWidget(self.skate_frame)
        self.cycle_frame = QtWidgets.QFrame(self.goals_overview_frame)
        self.cycle_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.cycle_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cycle_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cycle_frame.setObjectName("cycle_frame")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout(self.cycle_frame)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.label_21 = QtWidgets.QLabel(self.cycle_frame)
        self.label_21.setStyleSheet("QLabel {\n"
"    padding-right: 5px;\n"
"    font-size: 18px;\n"
"}")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_54.addWidget(self.label_21)
        self.cycle_progressBar = QtWidgets.QProgressBar(self.cycle_frame)
        self.cycle_progressBar.setStyleSheet("QProgressBar {\n"
"\n"
"    background-color: rgb(44, 49, 60);\n"
"    color: rgb(0,0,0);\n"
"    border: 1px solid rgb(28, 27, 27);\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(115, 210, 22, 255), stop:1 rgba(21, 92, 13, 255));\n"
"}")
        self.cycle_progressBar.setProperty("value", 0)
        self.cycle_progressBar.setObjectName("cycle_progressBar")
        self.horizontalLayout_54.addWidget(self.cycle_progressBar)
        spacerItem66 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem66)
        self.verticalLayout_19.addWidget(self.cycle_frame)
        self.actualizate_frame = QtWidgets.QFrame(self.goals_overview_frame)
        self.actualizate_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.actualizate_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.actualizate_frame.setObjectName("actualizate_frame")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.actualizate_frame)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        spacerItem67 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_55.addItem(spacerItem67)
        self.actualizate_button = QtWidgets.QPushButton(self.actualizate_frame)
        self.actualizate_button.setMinimumSize(QtCore.QSize(150, 20))
        self.actualizate_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(115, 210, 22, 150);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 0px solid rgba(115, 210, 22, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(115, 210, 22, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 100);\n"
"}")
        self.actualizate_button.setObjectName("actualizate_button")
        self.horizontalLayout_55.addWidget(self.actualizate_button)
        spacerItem68 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_55.addItem(spacerItem68)
        self.verticalLayout_19.addWidget(self.actualizate_frame)
        spacerItem69 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_19.addItem(spacerItem69)
        self.horizontalLayout_27.addWidget(self.goals_overview_frame)
        self.stackedWidget.addWidget(self.goals_overview_widget)
        self.registration_widget = QtWidgets.QWidget()
        self.registration_widget.setObjectName("registration_widget")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout(self.registration_widget)
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.registration_frame = QtWidgets.QFrame(self.registration_widget)
        self.registration_frame.setStyleSheet("border: none;")
        self.registration_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.registration_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.registration_frame.setObjectName("registration_frame")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.registration_frame)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_23 = QtWidgets.QLabel(self.registration_frame)
        self.label_23.setMinimumSize(QtCore.QSize(0, 80))
        self.label_23.setStyleSheet("QLabel {\n"
"    font-size: 30px;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_20.addWidget(self.label_23)
        self.frame_20 = QtWidgets.QFrame(self.registration_frame)
        self.frame_20.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        spacerItem70 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem70)
        self.label_28 = QtWidgets.QLabel(self.frame_20)
        self.label_28.setStyleSheet("QLabel {\n"
"    font-size: 15px;\n"
"}")
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_62.addWidget(self.label_28)
        spacerItem71 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem71)
        spacerItem72 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem72)
        self.verticalLayout_20.addWidget(self.frame_20)
        self.registration_name_frame = QtWidgets.QFrame(self.registration_frame)
        self.registration_name_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.registration_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.registration_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.registration_name_frame.setObjectName("registration_name_frame")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.registration_name_frame)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        spacerItem73 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_57.addItem(spacerItem73)
        self.label_24 = QtWidgets.QLabel(self.registration_name_frame)
        self.label_24.setStyleSheet("QLabel {\n"
"    font-size: 17px;\n"
"    padding-right: 15px;\n"
"}")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_57.addWidget(self.label_24)
        self.registration_name_edit = QtWidgets.QLineEdit(self.registration_name_frame)
        self.registration_name_edit.setMinimumSize(QtCore.QSize(620, 0))
        self.registration_name_edit.setMaximumSize(QtCore.QSize(620, 16777215))
        self.registration_name_edit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.registration_name_edit.setObjectName("registration_name_edit")
        self.horizontalLayout_57.addWidget(self.registration_name_edit)
        spacerItem74 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_57.addItem(spacerItem74)
        spacerItem75 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_57.addItem(spacerItem75)
        self.verticalLayout_20.addWidget(self.registration_name_frame)
        self.registration_surname_frame = QtWidgets.QFrame(self.registration_frame)
        self.registration_surname_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.registration_surname_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.registration_surname_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.registration_surname_frame.setObjectName("registration_surname_frame")
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout(self.registration_surname_frame)
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        spacerItem76 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_58.addItem(spacerItem76)
        self.label_25 = QtWidgets.QLabel(self.registration_surname_frame)
        self.label_25.setStyleSheet("QLabel {\n"
"    font-size: 17px;\n"
"    padding-right: 5px;\n"
"}")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_58.addWidget(self.label_25)
        self.registration_surname_edit = QtWidgets.QLineEdit(self.registration_surname_frame)
        self.registration_surname_edit.setMinimumSize(QtCore.QSize(620, 0))
        self.registration_surname_edit.setMaximumSize(QtCore.QSize(620, 16777215))
        self.registration_surname_edit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.registration_surname_edit.setObjectName("registration_surname_edit")
        self.horizontalLayout_58.addWidget(self.registration_surname_edit)
        spacerItem77 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_58.addItem(spacerItem77)
        spacerItem78 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_58.addItem(spacerItem78)
        self.verticalLayout_20.addWidget(self.registration_surname_frame)
        self.registration_height_frame = QtWidgets.QFrame(self.registration_frame)
        self.registration_height_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.registration_height_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.registration_height_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.registration_height_frame.setObjectName("registration_height_frame")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout(self.registration_height_frame)
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        spacerItem79 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_59.addItem(spacerItem79)
        self.label_26 = QtWidgets.QLabel(self.registration_height_frame)
        self.label_26.setStyleSheet("QLabel {\n"
"    font-size: 17px;\n"
"    padding-right: 23px;\n"
"}")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_59.addWidget(self.label_26)
        self.registration_height_edit = QtWidgets.QLineEdit(self.registration_height_frame)
        self.registration_height_edit.setMinimumSize(QtCore.QSize(620, 0))
        self.registration_height_edit.setMaximumSize(QtCore.QSize(620, 16777215))
        self.registration_height_edit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.registration_height_edit.setObjectName("registration_height_edit")
        self.horizontalLayout_59.addWidget(self.registration_height_edit)
        spacerItem80 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_59.addItem(spacerItem80)
        spacerItem81 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_59.addItem(spacerItem81)
        self.verticalLayout_20.addWidget(self.registration_height_frame)
        self.registration_weight_frame = QtWidgets.QFrame(self.registration_frame)
        self.registration_weight_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.registration_weight_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.registration_weight_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.registration_weight_frame.setObjectName("registration_weight_frame")
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout(self.registration_weight_frame)
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        spacerItem82 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_60.addItem(spacerItem82)
        self.label_27 = QtWidgets.QLabel(self.registration_weight_frame)
        self.label_27.setStyleSheet("QLabel {\n"
"    font-size: 17px;\n"
"    padding-right: 28px;\n"
"}")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_60.addWidget(self.label_27)
        self.registration_weight_edit = QtWidgets.QLineEdit(self.registration_weight_frame)
        self.registration_weight_edit.setMinimumSize(QtCore.QSize(620, 0))
        self.registration_weight_edit.setMaximumSize(QtCore.QSize(620, 16777215))
        self.registration_weight_edit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.registration_weight_edit.setObjectName("registration_weight_edit")
        self.horizontalLayout_60.addWidget(self.registration_weight_edit)
        spacerItem83 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_60.addItem(spacerItem83)
        spacerItem84 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_60.addItem(spacerItem84)
        self.verticalLayout_20.addWidget(self.registration_weight_frame)
        self.registration_create_frame = QtWidgets.QFrame(self.registration_frame)
        self.registration_create_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.registration_create_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.registration_create_frame.setObjectName("registration_create_frame")
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout(self.registration_create_frame)
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.registration_create_button = QtWidgets.QPushButton(self.registration_create_frame)
        self.registration_create_button.setMinimumSize(QtCore.QSize(150, 20))
        self.registration_create_button.setMaximumSize(QtCore.QSize(150, 20))
        self.registration_create_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(115, 210, 22, 150);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 0px solid rgba(115, 210, 22, 150);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(115, 210, 22, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 100);\n"
"}")
        self.registration_create_button.setObjectName("registration_create_button")
        self.horizontalLayout_61.addWidget(self.registration_create_button)
        self.verticalLayout_20.addWidget(self.registration_create_frame)
        spacerItem85 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem85)
        self.horizontalLayout_56.addWidget(self.registration_frame)
        self.stackedWidget.addWidget(self.registration_widget)
        self.horizontalLayout_9.addWidget(self.stackedWidget)
        self.verticalLayout_7.addWidget(self.central_content_frame)
        self.bottom_frame = QtWidgets.QFrame(self.content_frame)
        self.bottom_frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bottom_frame.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border: 0px;")
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem86 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem86)
        self.created_by_label = QtWidgets.QLabel(self.bottom_frame)
        self.created_by_label.setStyleSheet("QLabel{\n"
"    color: rgb(115, 210, 22);\n"
"    margin-right:5px;\n"
"}\n"
"")
        self.created_by_label.setObjectName("created_by_label")
        self.horizontalLayout_7.addWidget(self.created_by_label)
        self.verticalLayout_7.addWidget(self.bottom_frame)
        self.horizontalLayout_6.addWidget(self.content_frame)
        self.verticalLayout.addWidget(self.central_frame)
        self.verticalLayout_17.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.app_name_label.setText(_translate("MainWindow", "ITU - sports tracker"))
        self.file_path_label.setText(_translate("MainWindow", "/path/to/a/file"))
        self.title_user_label.setText(_translate("MainWindow", "Nastavení Uživatele"))
        self.name_label.setText(_translate("MainWindow", "Jméno"))
        self.surname_label.setText(_translate("MainWindow", "Příjmení"))
        self.height_label.setText(_translate("MainWindow", "Výška"))
        self.weight_label.setText(_translate("MainWindow", "Váha"))
        self.pushButton_3.setText(_translate("MainWindow", "Vymazat účet"))
        self.save_user_changes_button.setText(_translate("MainWindow", "Uložit změny"))
        self.user_foto_label.setText(_translate("MainWindow", "vložte fotku"))
        self.set_foto_button.setText(_translate("MainWindow", "Vložit fotku"))
        self.switch_user_button.setText(_translate("MainWindow", "Cíle"))
        self.label.setText(_translate("MainWindow", "Nastvení cílů"))
        self.label_2.setText(_translate("MainWindow", "Nastavení cílů pro danou sportovní aktivitu. Vyberte sport a zadejte počet minut za den."))
        self.sports_Box.setCurrentText(_translate("MainWindow", "Běh"))
        self.sports_Box.setItemText(0, _translate("MainWindow", "Běh"))
        self.sports_Box.setItemText(1, _translate("MainWindow", "Bruslení"))
        self.sports_Box.setItemText(2, _translate("MainWindow", "Chůze"))
        self.sports_Box.setItemText(3, _translate("MainWindow", "Cyklistika"))
        self.set_goals_button.setText(_translate("MainWindow", "Nastavit"))
        self.switch_goals_button.setText(_translate("MainWindow", "Uživatel"))
        self.profile_foto_label.setText(_translate("MainWindow", "Profilová fotka"))
        self.label_4.setText(_translate("MainWindow", "Jméno:"))
        self.label_5.setText(_translate("MainWindow", "Přijmení:"))
        self.label_6.setText(_translate("MainWindow", "Výška:"))
        self.label_32.setText(_translate("MainWindow", "cm"))
        self.label_7.setText(_translate("MainWindow", "Šířka:"))
        self.label_33.setText(_translate("MainWindow", "kg"))
        self.label_12.setText(_translate("MainWindow", "Běh:"))
        self.label_22.setText(_translate("MainWindow", "min"))
        self.label_14.setText(_translate("MainWindow", "Bruslení:"))
        self.label_29.setText(_translate("MainWindow", "min"))
        self.label_16.setText(_translate("MainWindow", "Chůze:"))
        self.label_30.setText(_translate("MainWindow", "min"))
        self.label_18.setText(_translate("MainWindow", "Cyklistika:"))
        self.label_31.setText(_translate("MainWindow", "min"))
        self.timer_label.setText(_translate("MainWindow", "00:00"))
        self.timer_box.setItemText(0, _translate("MainWindow", "Běh"))
        self.timer_box.setItemText(1, _translate("MainWindow", "Bruslení"))
        self.timer_box.setItemText(2, _translate("MainWindow", "Chůze"))
        self.timer_box.setItemText(3, _translate("MainWindow", "Cyklistika"))
        self.timer_start_button.setText(_translate("MainWindow", "Start"))
        self.timer_stop_button.setText(_translate("MainWindow", "Stop"))
        self.timer_reset_button.setText(_translate("MainWindow", "Reset"))
        self.timer_save_button.setText(_translate("MainWindow", "Uložit"))
        self.timer_data_insert_button_2.setText(_translate("MainWindow", "Uložit změřenou aktivitu"))
        self.label_3.setText(_translate("MainWindow", "Uložení aktivity"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Běh"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Bruslení"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Chůze"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Cyklistika"))
        self.label_9.setText(_translate("MainWindow", "Počet odcvičených minut: "))
        self.pushButton_2.setText(_translate("MainWindow", "Uložit"))
        self.pushButton.setText(_translate("MainWindow", "Změřit čas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.week_tab), _translate("MainWindow", "Týden"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.month_tab), _translate("MainWindow", "Měsíc"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.year_tab), _translate("MainWindow", "Rok"))
        self.graphs_box.setItemText(0, _translate("MainWindow", "Běh"))
        self.graphs_box.setItemText(1, _translate("MainWindow", "Bruslení"))
        self.graphs_box.setItemText(2, _translate("MainWindow", "Chůze"))
        self.graphs_box.setItemText(3, _translate("MainWindow", "Cyklistika"))
        self.graphs_generate_button.setText(_translate("MainWindow", "Vygenerovat"))
        self.label_8.setText(_translate("MainWindow", "Denní cíle"))
        self.label_10.setText(_translate("MainWindow", "Běh:"))
        self.label_20.setText(_translate("MainWindow", "Chůze:"))
        self.label_11.setText(_translate("MainWindow", "Bruslení:"))
        self.label_21.setText(_translate("MainWindow", "Cyklistika:"))
        self.actualizate_button.setText(_translate("MainWindow", "Aktualizovat"))
        self.label_23.setText(_translate("MainWindow", "Registrace"))
        self.label_28.setText(_translate("MainWindow", "Jsi tu nový! Vítej. Vyplň své údaje."))
        self.label_24.setText(_translate("MainWindow", "Jméno:"))
        self.label_25.setText(_translate("MainWindow", "Příjmení:"))
        self.label_26.setText(_translate("MainWindow", "Výška:"))
        self.label_27.setText(_translate("MainWindow", "Váha:"))
        self.registration_create_button.setText(_translate("MainWindow", "Vytvořit"))
        self.created_by_label.setText(_translate("MainWindow", "Created by: Tym xburka00"))
from pyqtgraph import PlotWidget
