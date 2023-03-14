# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Ziad\Documents\GitHub\TimeTrackingProject\UI\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginUI(object):
    def setupUi(self, loginUI):
        loginUI.setObjectName("loginUI")
        loginUI.resize(795, 600)
        loginUI.setStyleSheet("background-color: rgb(133, 92, 119);")
        self.leftSide = QtWidgets.QWidget(loginUI)
        self.leftSide.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.leftSide.setStyleSheet("background-color: #4D455D;\n"
"border-right-color: rgb(27, 0, 21);\n"
"")
        self.leftSide.setObjectName("leftSide")
        self.imageFrame = QtWidgets.QFrame(self.leftSide)
        self.imageFrame.setGeometry(QtCore.QRect(0, 160, 401, 441))
        self.imageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageFrame.setObjectName("imageFrame")
        self.image = QtWidgets.QLabel(self.imageFrame)
        self.image.setGeometry(QtCore.QRect(0, 0, 401, 441))
        self.image.setStyleSheet("border-radius:50px;")
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("c:\\Users\\Ziad\\Documents\\GitHub\\TimeTrackingProject\\UI\\images/pomodoro.png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.titleWidget = QtWidgets.QWidget(self.leftSide)
        self.titleWidget.setEnabled(True)
        self.titleWidget.setGeometry(QtCore.QRect(20, 10, 351, 121))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.titleWidget.setFont(font)
        self.titleWidget.setStyleSheet("\n"
"color:#F5E9CF;\n"
"\n"
"")
        self.titleWidget.setObjectName("titleWidget")
        self.timeTrackingText = QtWidgets.QLabel(self.titleWidget)
        self.timeTrackingText.setGeometry(QtCore.QRect(-10, 20, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(False)
        self.timeTrackingText.setFont(font)
        self.timeTrackingText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timeTrackingText.setAlignment(QtCore.Qt.AlignCenter)
        self.timeTrackingText.setObjectName("timeTrackingText")
        self.timeTrackingText_2 = QtWidgets.QLabel(self.titleWidget)
        self.timeTrackingText_2.setGeometry(QtCore.QRect(-10, 70, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(False)
        self.timeTrackingText_2.setFont(font)
        self.timeTrackingText_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timeTrackingText_2.setStyleSheet("color:#F5E9CF;\n"
"")
        self.timeTrackingText_2.setAlignment(QtCore.Qt.AlignCenter)
        self.timeTrackingText_2.setObjectName("timeTrackingText_2")
        self.rightSide = QtWidgets.QWidget(loginUI)
        self.rightSide.setGeometry(QtCore.QRect(400, 0, 400, 600))
        self.rightSide.setStyleSheet("background-color:#4D455D;")
        self.rightSide.setObjectName("rightSide")
        self.signUpWidget = QtWidgets.QWidget(self.rightSide)
        self.signUpWidget.setEnabled(True)
        self.signUpWidget.setGeometry(QtCore.QRect(10, 310, 380, 280))
        self.signUpWidget.setStyleSheet("background-color:#7DB9B6;\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"")
        self.signUpWidget.setObjectName("signUpWidget")
        self.signUpButton = QtWidgets.QPushButton(self.signUpWidget)
        self.signUpButton.setGeometry(QtCore.QRect(140, 230, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Chalkboard")
        font.setPointSize(14)
        self.signUpButton.setFont(font)
        self.signUpButton.setStyleSheet("background-color:#F5E9CF;\n"
"border-radius:10px;\n"
"color:#4D455D;")
        self.signUpButton.setObjectName("signUpButton")
        self.emailInputSignUp = QtWidgets.QLineEdit(self.signUpWidget)
        self.emailInputSignUp.setGeometry(QtCore.QRect(40, 170, 311, 31))
        self.emailInputSignUp.setStyleSheet("background-color: rgba(217, 217, 217, 66);\n"
"border-radius:10px;\n"
"")
        self.emailInputSignUp.setText("")
        self.emailInputSignUp.setObjectName("emailInputSignUp")
        self.emailTextLabel = QtWidgets.QLabel(self.signUpWidget)
        self.emailTextLabel.setGeometry(QtCore.QRect(50, 140, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Chalkboard")
        font.setPointSize(14)
        font.setUnderline(False)
        self.emailTextLabel.setFont(font)
        self.emailTextLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.emailTextLabel.setObjectName("emailTextLabel")
        self.signUpTextLAbel = QtWidgets.QLabel(self.signUpWidget)
        self.signUpTextLAbel.setGeometry(QtCore.QRect(120, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Chalkboard")
        font.setPointSize(20)
        font.setUnderline(False)
        self.signUpTextLAbel.setFont(font)
        self.signUpTextLAbel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.signUpTextLAbel.setAlignment(QtCore.Qt.AlignCenter)
        self.signUpTextLAbel.setObjectName("signUpTextLAbel")
        self.errorTextSignUp = QtWidgets.QLineEdit(self.signUpWidget)
        self.errorTextSignUp.setGeometry(QtCore.QRect(50, 200, 301, 21))
        self.errorTextSignUp.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color:red;")
        self.errorTextSignUp.setText("")
        self.errorTextSignUp.setReadOnly(True)
        self.errorTextSignUp.setObjectName("errorTextSignUp")
        self.nameTextLabel = QtWidgets.QLabel(self.signUpWidget)
        self.nameTextLabel.setGeometry(QtCore.QRect(50, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Chalkboard")
        font.setPointSize(14)
        font.setUnderline(False)
        self.nameTextLabel.setFont(font)
        self.nameTextLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nameTextLabel.setObjectName("nameTextLabel")
        self.nameInputSignUp = QtWidgets.QLineEdit(self.signUpWidget)
        self.nameInputSignUp.setGeometry(QtCore.QRect(40, 100, 311, 31))
        self.nameInputSignUp.setStyleSheet("background-color: rgba(217, 217, 217, 66);\n"
"border-radius:10px;\n"
"")
        self.nameInputSignUp.setText("")
        self.nameInputSignUp.setObjectName("nameInputSignUp")
        self.loginWidget = QtWidgets.QWidget(self.rightSide)
        self.loginWidget.setEnabled(True)
        self.loginWidget.setGeometry(QtCore.QRect(10, 10, 380, 280))
        self.loginWidget.setStyleSheet("background-color:#E96479;\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;\n"
"")
        self.loginWidget.setObjectName("loginWidget")
        self.loginButton = QtWidgets.QPushButton(self.loginWidget)
        self.loginButton.setGeometry(QtCore.QRect(150, 220, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Chalkboard")
        font.setPointSize(14)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background-color:#F5E9CF;\n"
"border-radius:10px;\n"
"color:#4D455D;")
        self.loginButton.setObjectName("loginButton")
        self.emailInputLogin = QtWidgets.QLineEdit(self.loginWidget)
        self.emailInputLogin.setGeometry(QtCore.QRect(40, 140, 311, 31))
        self.emailInputLogin.setStyleSheet("background-color: rgba(217, 217, 217, 66);\n"
"border-radius:10px;\n"
"")
        self.emailInputLogin.setText("")
        self.emailInputLogin.setObjectName("emailInputLogin")
        self.emailLabel = QtWidgets.QLabel(self.loginWidget)
        self.emailLabel.setGeometry(QtCore.QRect(50, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Chalkboard")
        font.setPointSize(14)
        font.setUnderline(False)
        self.emailLabel.setFont(font)
        self.emailLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.emailLabel.setObjectName("emailLabel")
        self.loginText = QtWidgets.QLabel(self.loginWidget)
        self.loginText.setGeometry(QtCore.QRect(140, 30, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Chalkboard")
        font.setPointSize(20)
        font.setUnderline(False)
        self.loginText.setFont(font)
        self.loginText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loginText.setAlignment(QtCore.Qt.AlignCenter)
        self.loginText.setObjectName("loginText")
        self.errorTextLogin = QtWidgets.QLineEdit(self.loginWidget)
        self.errorTextLogin.setGeometry(QtCore.QRect(50, 170, 301, 21))
        self.errorTextLogin.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color:black;")
        self.errorTextLogin.setText("")
        self.errorTextLogin.setReadOnly(True)
        self.errorTextLogin.setObjectName("errorTextLogin")

        self.retranslateUi(loginUI)
        QtCore.QMetaObject.connectSlotsByName(loginUI)

    def retranslateUi(self, loginUI):
        _translate = QtCore.QCoreApplication.translate
        loginUI.setWindowTitle(_translate("loginUI", "Widget"))
        self.timeTrackingText.setText(_translate("loginUI", "Time Tracking"))
        self.timeTrackingText_2.setText(_translate("loginUI", "Pomodoro"))
        self.signUpButton.setText(_translate("loginUI", "Sign Up"))
        self.emailTextLabel.setText(_translate("loginUI", "Email:"))
        self.signUpTextLAbel.setText(_translate("loginUI", "Sign Up"))
        self.nameTextLabel.setText(_translate("loginUI", "Name:"))
        self.loginButton.setText(_translate("loginUI", "Login"))
        self.emailLabel.setText(_translate("loginUI", "Email:"))
        self.loginText.setText(_translate("loginUI", "Login"))