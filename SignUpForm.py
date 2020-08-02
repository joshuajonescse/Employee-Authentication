'''
 * @author Joshua Jones
 * Created Date: feb, 2020
 * mail me at joshuajonesegbert@gmail.com in case of any PR or query

 '''

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_DialogSignUp(object):

    def signupAction(self):
        username = self.uname_lineEdit.text()
        password = self.pass_lineEdit_2.text()
        email = self.email_lineEdit_3.text()
        connection = sqlite3.connect("userLogin.db")
        connection.execute("INSERT INTO Employees VALUES(?,?,?)", (username,email,password))
        connection.commit()
        connection.close()
        print("Credentials Entered")


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(773, 496)
        Dialog.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"background-color: rgb(170, 170, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 40, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(255, 0, 0);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.signup_pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.signup_pushButton_2.setGeometry(QtCore.QRect(350, 360, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signup_pushButton_2.setFont(font)
        self.signup_pushButton_2.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.signup_pushButton_2.setObjectName("signup_pushButton_2")
        self.signup_pushButton_2.clicked.connect(self.signupAction)
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(390, 160, 113, 20))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.USER_LABEL = QtWidgets.QLabel(Dialog)
        self.USER_LABEL.setGeometry(QtCore.QRect(240, 162, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.USER_LABEL.setFont(font)
        self.USER_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.USER_LABEL.setObjectName("USER_LABEL")
        self.pass_lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit_2.setGeometry(QtCore.QRect(390, 210, 113, 20))
        self.pass_lineEdit_2.setObjectName("pass_lineEdit_2")
        self.PASS_LABEL = QtWidgets.QLabel(Dialog)
        self.PASS_LABEL.setGeometry(QtCore.QRect(240, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.PASS_LABEL.setFont(font)
        self.PASS_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.PASS_LABEL.setObjectName("PASS_LABEL")
        self.email_lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.email_lineEdit_3.setGeometry(QtCore.QRect(390, 270, 113, 20))
        self.email_lineEdit_3.setObjectName("email_lineEdit_3")
        self.PASS_LABEL_2 = QtWidgets.QLabel(Dialog)
        self.PASS_LABEL_2.setGeometry(QtCore.QRect(230, 270, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.PASS_LABEL_2.setFont(font)
        self.PASS_LABEL_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PASS_LABEL_2.setObjectName("PASS_LABEL_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SignUp Form"))
        self.label.setText(_translate("Dialog", "Register New Account "))
        self.signup_pushButton_2.setText(_translate("Dialog", "SignUp"))
        self.USER_LABEL.setText(_translate("Dialog", "USERNAME"))
        self.PASS_LABEL.setText(_translate("Dialog", "PASSWORD"))
        self.PASS_LABEL_2.setText(_translate("Dialog", "EMAIL ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogSignUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
