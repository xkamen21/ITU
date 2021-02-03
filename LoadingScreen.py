# Subject: ITU
# School:  Faculty of Information Technology, Brno University of Technology
# Authors: Boris Burkalo
#          Daniel Kamenický
#          Jan Klusáček
#
# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.15.2

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadingScreen(object):
    def setupUi(self, LoadingScreen):
        LoadingScreen.setObjectName("LoadingScreen")
        LoadingScreen.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(LoadingScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame {\n"
"    background-color: rgb(44, 49, 60);\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.label_title = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_title.setGeometry(QtCore.QRect(0, 120, 661, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(115, 210, 22);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_description = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_description.setGeometry(QtCore.QRect(0, 200, 661, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(98, 114, 164);\n"
"color: rgb(186, 189, 182)")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(50, 280, 561, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
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
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_loading.setGeometry(QtCore.QRect(0, 320, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("color: rgb(186, 189, 182);")
        self.label_loading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.label_credits = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_credits.setGeometry(QtCore.QRect(20, 350, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(186, 189, 182);")
        self.label_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.label_title_2 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_title_2.setGeometry(QtCore.QRect(5, 50, 650, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title_2.setFont(font)
        self.label_title_2.setStyleSheet("color: rgb(115, 210, 22);")
        self.label_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_2.setObjectName("label_title_2")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        LoadingScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadingScreen)
        QtCore.QMetaObject.connectSlotsByName(LoadingScreen)

    def retranslateUi(self, LoadingScreen):
        _translate = QtCore.QCoreApplication.translate
        LoadingScreen.setWindowTitle(_translate("LoadingScreen", "MainWindow"))
        self.label_title.setText(_translate("LoadingScreen", "<html><head/><body><p>sports tracker</p></body></html>"))
        self.label_description.setText(_translate("LoadingScreen", "<strong>APP</strong> DESCRIPTION"))
        self.label_loading.setText(_translate("LoadingScreen", "loading..."))
        self.label_credits.setText(_translate("LoadingScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Created</span>: tym xburka00</p><p><br/></p></body></html>"))
        self.label_title_2.setText(_translate("LoadingScreen", "<html><head/><body><p><span style=\" font-weight:600;\">ITU</span></p></body></html>"))
