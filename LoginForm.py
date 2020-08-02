
'''
 * @ author Joshua Jones
 * Created Date: feb, 2020
 * mail me at joshuajonesegbert@gmail.com in case of any query

 '''

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from SignUpForm import Ui_DialogSignUp
from Welcome import Ui_MainWindow

class Ui_Dialog(object):

    def helloWindowShow(self):
        self.HelloWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.HelloWindow)
        self.HelloWindow.show()

    def messageBox(self,title,message):
        messageObj = QtWidgets.QMessageBox()
        messageObj.setIcon(QtWidgets.QMessageBox.Warning)
        messageObj.setWindowTitle(title)
        messageObj.setText(message)
        messageObj.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messageObj.exec_()

    def checkLogin(self):
        username = self.user_lineEdit.text()
        password = self.password_lineEdit_2.text()
        connection = sqlite3.connect("userLogin.db")
        result = connection.execute("SELECT * FROM Employees WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        if (len(result.fetchall())>0):
            self.helloWindowShow()
        else:
            self.messageBox('Warning', 'Invalid Employee Credentials')

    def signupOpen(self):
        self.signUpWin = QtWidgets.QDialog()
        self.ui = Ui_DialogSignUp()
        self.ui.setupUi(self.signUpWin)
        self.signUpWin.show()


    def checkSignUp(self):
        self.signupOpen()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(772, 488)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"background-color: rgb(170, 170, 127);")
        self.USER_LABEL = QtWidgets.QLabel(Dialog)
        self.USER_LABEL.setGeometry(QtCore.QRect(230, 162, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.USER_LABEL.setFont(font)
        self.USER_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.USER_LABEL.setObjectName("USER_LABEL")
        self.PASS_LABEL = QtWidgets.QLabel(Dialog)
        self.PASS_LABEL.setGeometry(QtCore.QRect(230, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.PASS_LABEL.setFont(font)
        self.PASS_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.PASS_LABEL.setObjectName("PASS_LABEL")
        self.user_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.user_lineEdit.setGeometry(QtCore.QRect(380, 160, 113, 20))
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.password_lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit_2.setGeometry(QtCore.QRect(380, 210, 113, 20))
        self.password_lineEdit_2.setObjectName("password_lineEdit_2")
       # self.password_lineEdit_2.setEchoMode()
        self.login_pushButton = QtWidgets.QPushButton(Dialog)
        self.login_pushButton.setGeometry(QtCore.QRect(270, 320, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_pushButton.setFont(font)
        self.login_pushButton.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.login_pushButton.setObjectName("login_pushButton")
        '''Adding the event to the login button'''
        self.login_pushButton.clicked.connect(self.checkLogin)
        self.signup_pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.signup_pushButton_2.setGeometry(QtCore.QRect(380, 320, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signup_pushButton_2.setFont(font)
        self.signup_pushButton_2.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.signup_pushButton_2.setObjectName("signup_pushButton_2")
        '''Adding the event to the login button'''
        self.signup_pushButton_2.clicked.connect(self.checkSignUp)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 50, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(255, 0, 0);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login Form"))
        self.USER_LABEL.setText(_translate("Dialog", "USERNAME"))
        self.PASS_LABEL.setText(_translate("Dialog", "PASSWORD"))
        self.login_pushButton.setText(_translate("Dialog", "Login"))
        self.signup_pushButton_2.setText(_translate("Dialog", "SignUp"))
        self.label.setText(_translate("Dialog", "Employee Login Form "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
