# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import MainWindow
import datahandle

class Ui_LogIn(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(658, 309)

        self.label_user = QtWidgets.QLabel(Form)
        self.label_user.setGeometry(QtCore.QRect(180, 50, 81, 31))
        self.label_user.setObjectName("label_user")
        self.label_password = QtWidgets.QLabel(Form)
        self.label_password.setGeometry(QtCore.QRect(180, 90, 91, 41))
        self.label_password.setObjectName("label_password")
        self.pt_login = QtWidgets.QPushButton(Form)
        self.pt_login.setGeometry(QtCore.QRect(180, 190, 93, 28))
        self.pt_login.setObjectName("login")
        self.line_user = QtWidgets.QLineEdit(Form)
        self.line_user.setGeometry(QtCore.QRect(240, 50, 201, 21))
        self.line_user.setObjectName("line_user")
        self.line_password = QtWidgets.QLineEdit(Form)
        self.line_password.setGeometry(QtCore.QRect(240, 100, 201, 21))
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setObjectName("line_password")
        self.pt_exit = QtWidgets.QPushButton(Form)
        self.pt_exit.setGeometry(QtCore.QRect(350, 190, 93, 28))
        self.pt_exit.setObjectName("exit")
        self.box_showpassword = QtWidgets.QCheckBox(Form)
        self.box_showpassword.setGeometry(QtCore.QRect(280, 140, 92, 21))
        self.box_showpassword.setObjectName("box_showpassword")

        self.retranslateUi(Form)

        self.pt_login.clicked.connect(lambda: self.checkuserpassword(Form))

        self.pt_login.clicked.connect(self.line_password.clear)
        self.pt_exit.clicked.connect(Form.close)

        self.box_showpassword.stateChanged['int'].connect(self.change_echoMode)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def change_echoMode(self):
        if self.box_showpassword.isChecked():
            self.line_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_user.setText(_translate("Form", "用户名"))
        self.label_password.setText(_translate("Form", "密码"))
        self.pt_login.setText(_translate("Form", "登录"))
        self.pt_exit.setText(_translate("Form", "退出"))
        self.box_showpassword.setText(_translate("Form", "显示密码"))

    def checkuserpassword(self,Form):
        self.user=self.line_user.text()
        self.password=self.line_password.text()
        txt=self.user+'/'+self.password+'@3316jf2639.qicp.vip:21413/demo'
        try:
            self.abc=datahandle.dataoperate()
            self.abc.initial(txt)
            QtWidgets.QMessageBox.information(Form, 'Message',
                                              "Successfully login!")

            Form.close()  # 若成功关闭登录界面
            self.jump_mainwindow(Form)
        except:
            QtWidgets.QMessageBox.information(Form, 'Message',
                                              "Invalid username/password")
    def getuser(self):
        return self.user
    def getpassward(self):
        return self.password
    def jump_mainwindow(self, Form):
        """
        Form: 登录窗口
        return:
        """
        self.main_wd = QMainWindow()
        self.ui_main_wd = MainWindow.Ui_MainWindow()
        self.ui_main_wd.setupUi(self.main_wd)
        self.ui_main_wd.initial(self.abc)
        self.main_wd.show()
        self.ui_main_wd.action_relog.triggered.connect(Form.show)
        self.ui_main_wd.action_relog.triggered.connect(Form.raise_)
        self.ui_main_wd.action_relog.triggered.connect(self.line_user.clear)
        self.ui_main_wd.action_relog.triggered.connect(self.line_password.clear)
        self.ui_main_wd.password = self.password
