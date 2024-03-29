# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keep_use.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import SealStandards, SealFactory, SealManager


class Ui_KeepUse(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(599, 420)
        self.stands = QtWidgets.QPushButton(Dialog)
        self.stands.setGeometry(QtCore.QRect(130, 80, 301, 61))
        self.stands.setObjectName("stands")
        self.company = QtWidgets.QPushButton(Dialog)
        self.company.setGeometry(QtCore.QRect(130, 190, 301, 61))
        self.company.setObjectName("company")
        self.information = QtWidgets.QPushButton(Dialog)
        self.information.setGeometry(QtCore.QRect(130, 300, 301, 61))
        self.information.setObjectName("information")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(150, 0, 271, 61))
        self.title.setObjectName("title")

        self.retranslateUi(Dialog)

        self.stands_form = None
        self.stands.clicked.connect(self.jump_to_stands)
        self.company_form = None
        self.company.clicked.connect(self.jump_to_company)
        self.information_form = None
        self.information.clicked.connect(self.jump_to_information)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def jump_to_stands(self):
        if self.stands_form == None:
            self.stands_form = QtWidgets.QMainWindow()
            self.ui = SealStandards.Ui_SealStandards()
            self.ui.innitial(self.data)
            self.ui.setupUi(self.stands_form)
            self.stands_form.show()
        elif isinstance(self.stands_form, QtWidgets.QMainWindow):
            self.stands_form.show()
            self.stands_form.raise_()

    def jump_to_company(self):
        if self.company_form == None:
            self.company_form = QtWidgets.QMainWindow()
            self.ui = SealFactory.Ui_SealFactory()
            self.ui.innitial(self.data)
            self.ui.setupUi(self.company_form)
            self.company_form.show()
        elif isinstance(self.company_form, QtWidgets.QMainWindow):
            self.company_form.show()
            self.company_form.raise_()

    def jump_to_information(self):
        if self.information_form == None:
            self.information_form = QtWidgets.QMainWindow()
            self.ui = SealManager.Ui_SealManager()
            self.ui.innitial(self.data)
            self.ui.setupUi(self.information_form)
            self.information_form.show()
        elif isinstance(self.information_form, QtWidgets.QMainWindow):
            self.information_form.show()
            self.information_form.raise_()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.stands.setText(_translate("Dialog", "印章标准管理"))
        self.company.setText(_translate("Dialog", "印章厂家管理"))
        self.information.setText(_translate("Dialog", "印章信息管理"))
        self.title.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'黑体\'; font-size:14pt; font-weight:600;\">印章保管与使用标准管理 </span></p></body></html>"))
        self.title.setWhatsThis(_translate("Dialog", "<html><head/><body><p>sdasdasdasdasd</p></body></html>"))
        self.title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">印章保管与使用标准管理 </span></p></body></html>"))
    def innitial(self,u):
        self.data=u
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    handover = QtWidgets.QMainWindow()
    ui_handover = Ui_KeepUse()
    ui_handover.setupUi(handover)
    handover.show()
    sys.exit(app.exec_())