# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sealmanager.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import datahandle
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from qtpy.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QMainWindow,
                             QTableWidgetItem, QAbstractItemView, QPushButton)
from PyQt5.QtCore import QDate

class Ui_SealManager(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1148, 659)
        self.Form = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 100, 301, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(149)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 120, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 0, 201, 61))
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 60, 301, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(370, 150, 421, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rpt_disabled = QtWidgets.QRadioButton(self.widget1)
        self.rpt_disabled.setObjectName("rpt_disabled")
        self.horizontalLayout_2.addWidget(self.rpt_disabled)
        self.rpt_enabled = QtWidgets.QRadioButton(self.widget1)
        self.rpt_enabled.setObjectName("rpt_enabled")
        self.horizontalLayout_2.addWidget(self.rpt_enabled)
        self.rpt_deact = QtWidgets.QRadioButton(self.widget1)
        self.rpt_deact.setObjectName("rpt_deact")
        self.horizontalLayout_2.addWidget(self.rpt_deact)
        self.rpt_maint = QtWidgets.QRadioButton(self.widget1)
        self.rpt_maint.setObjectName("rpt_maint")
        self.horizontalLayout_2.addWidget(self.rpt_maint)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(370, 60, 421, 26))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.line_SealName = QtWidgets.QLineEdit(self.widget2)
        self.line_SealName.setObjectName("line_SealName")
        self.horizontalLayout_3.addWidget(self.line_SealName)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(370, 190, 741, 201))
        self.widget3.setObjectName("widget3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget3)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.cb_type = QtWidgets.QComboBox(self.widget3)
        self.cb_type.setObjectName("cb_type")
        self.gridLayout.addWidget(self.cb_type, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget3)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)
        self.cb_shape = QtWidgets.QComboBox(self.widget3)
        self.cb_shape.setObjectName("cb_shape")
        self.gridLayout.addWidget(self.cb_shape, 0, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget3)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 4, 1, 1)
        self.cb_size = QtWidgets.QComboBox(self.widget3)
        self.cb_size.setObjectName("cb_size")
        self.gridLayout.addWidget(self.cb_size, 0, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget3)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.cb_mat = QtWidgets.QComboBox(self.widget3)
        self.cb_mat.setObjectName("cb_mat")
        self.gridLayout.addWidget(self.cb_mat, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget3)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.cb_font = QtWidgets.QComboBox(self.widget3)
        self.cb_font.setObjectName("cb_font")
        self.gridLayout.addWidget(self.cb_font, 1, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget3)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 4, 1, 1)
        self.cb_use = QtWidgets.QComboBox(self.widget3)
        self.cb_use.setObjectName("cb_use")
        self.gridLayout.addWidget(self.cb_use, 1, 5, 1, 1)
        self.lb_time_s = QtWidgets.QLabel(self.widget3)
        self.lb_time_s.setObjectName("lb_time_s")
        self.gridLayout.addWidget(self.lb_time_s, 2, 0, 1, 1)
        self.cb_time_s = QtWidgets.QDateEdit(self.widget3)
        self.cb_time_s.setObjectName("cb_time_s")
        self.gridLayout.addWidget(self.cb_time_s, 2, 1, 1, 1)
        self.lb_original_dept = QtWidgets.QLabel(self.widget3)
        self.lb_original_dept.setObjectName("lb_original_dept")
        self.gridLayout.addWidget(self.lb_original_dept, 2, 2, 1, 1)
        self.cb_original_dept = QtWidgets.QComboBox(self.widget3)
        self.cb_original_dept.setObjectName("cb_original_dept")
        self.gridLayout.addWidget(self.cb_original_dept, 2, 3, 1, 1)
        self.lb_keeper = QtWidgets.QLabel(self.widget3)
        self.lb_keeper.setObjectName("lb_keeper")
        self.gridLayout.addWidget(self.lb_keeper, 2, 4, 1, 1)
        self.cb_keeper = QtWidgets.QComboBox(self.widget3)
        self.cb_keeper.setObjectName("cb_keeper")
        self.gridLayout.addWidget(self.cb_keeper, 2, 5, 1, 1)
        self.lb_time_e = QtWidgets.QLabel(self.widget3)
        self.lb_time_e.setObjectName("lb_time_e")
        self.gridLayout.addWidget(self.lb_time_e, 3, 0, 1, 1)
        self.cb_time_e = QtWidgets.QDateEdit(self.widget3)
        self.cb_time_e.setObjectName("cb_time_e")
        self.gridLayout.addWidget(self.cb_time_e, 3, 1, 1, 1)
        self.lb_keep_dept = QtWidgets.QLabel(self.widget3)
        self.lb_keep_dept.setObjectName("lb_keep_dept")
        self.gridLayout.addWidget(self.lb_keep_dept, 3, 2, 1, 1)
        self.cb_keep_dept = QtWidgets.QComboBox(self.widget3)
        self.cb_keep_dept.setObjectName("cb_keep_dept")
        self.gridLayout.addWidget(self.cb_keep_dept, 3, 3, 1, 1)
        self.lb_saved = QtWidgets.QLabel(self.widget3)
        self.lb_saved.setObjectName("lb_saved")
        self.gridLayout.addWidget(self.lb_saved, 3, 4, 1, 1)
        self.cb_saved = QtWidgets.QComboBox(self.widget3)
        self.cb_saved.setObjectName("cb_saved")
        self.gridLayout.addWidget(self.cb_saved, 3, 5, 1, 1)
        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(540, 440, 195, 91))
        self.widget4.setObjectName("widget4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pb_new = QtWidgets.QPushButton(self.widget4)
        self.pb_new.setEnabled(True)
        self.pb_new.setObjectName("pb_new")
        self.gridLayout_2.addWidget(self.pb_new, 0, 0, 1, 1)
        self.pb_add = QtWidgets.QPushButton(self.widget4)
        self.pb_add.setEnabled(False)
        self.pb_add.setObjectName("pb_add")
        self.gridLayout_2.addWidget(self.pb_add, 0, 1, 1, 1)
        self.pb_change = QtWidgets.QPushButton(self.widget4)
        self.pb_change.setEnabled(True)
        self.pb_change.setObjectName("pb_change")
        self.gridLayout_2.addWidget(self.pb_change, 1, 0, 1, 1)
        self.pb_del = QtWidgets.QPushButton(self.widget4)
        self.pb_del.setEnabled(True)
        self.pb_del.setObjectName("pb_del")
        self.gridLayout_2.addWidget(self.pb_del, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1148, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #下面是选择停用选项时才会出现的
        self.deact_cb_group = [self.cb_time_s, self.cb_time_e,
                               self.cb_original_dept,self.cb_keeper,
                               self.cb_keep_dept,self.cb_saved]

        self.deact_lb_group = [self.lb_time_s, self.lb_time_e,
                               self.lb_original_dept, self.lb_keeper,
                               self.lb_keep_dept, self.lb_saved]

        for cb in self.deact_cb_group:
            cb.setVisible(False)
            cb.setEnabled(False)

        for lb in self.deact_lb_group:
            lb.setVisible(False)


        self.pb_new.setEnabled(True)
        self.pb_change.setEnabled(False)
        self.pb_del.setEnabled(False)
        self.rpt_deact.setEnabled(False)
        self.rpt_disabled.setEnabled(False)
        self.rpt_enabled.setEnabled(False)
        self.rpt_maint.setEnabled(False)
        self.rpt_deact.toggled.connect(lambda: self.btnstate(self.rpt_deact))

        self.state = None #印章状态
        self.deact_group = [self.line_SealName,self.cb_time_s, self.cb_time_e,
                       self.cb_original_dept,self.cb_keeper, self.cb_keep_dept,
                       self.cb_saved, self.cb_shape, self.cb_type,
                       self.cb_size, self.cb_mat,self.cb_font,self.cb_use]
        #停用涉及到数据所有数据

        self.cb_group = [self.cb_type, self.cb_shape, self.cb_size, self.cb_mat,
                         self.cb_font, self.cb_use,self.cb_time_s, self.cb_time_e,
                         self.cb_original_dept,self.cb_keeper, self.cb_keep_dept,
                         self.cb_saved]  #后续所有combo_box都需要放进去

        #for line in self.area_A:
        #    self.pb_new.clicked['bool'].connect(line.setDisabled)
        self.line_SealName.setEnabled(False)
        self.cursor = self.data.cursor
        self.cursor.execute("select *from seal")
        self.insertindex=len(self.cursor.fetchall())
        self.pb_new.clicked['bool'].connect(self.pb_add.setDisabled)
        self.pb_new.clicked['bool'].connect(self.pb_new.setEnabled)
        self.pb_new.clicked['bool'].connect(self.line_SealName.clear)
        self.pb_new.clicked['bool'].connect(self.click_pb_new)
        self.pb_add.clicked['bool'].connect(self.table_add)
        self.pb_del.clicked['bool'].connect(self.table_del)
        self.pb_change.clicked['bool'].connect(self.table_change)
        self.tableWidget.clicked.connect(self.table_slot)

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "印章编码"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "印章名称"))
        self.label_3.setText(_translate("MainWindow", "印章状态"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt; font-weight:600;\">印章管理</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "印章编码/名称"))
        self.pushButton.setText(_translate("MainWindow", "刷新"))
        self.rpt_disabled.setText(_translate("MainWindow", "未启用"))
        self.rpt_enabled.setText(_translate("MainWindow", "启用"))
        self.rpt_deact.setText(_translate("MainWindow", "停用"))
        self.rpt_maint.setText(_translate("MainWindow", "刻制或维修中"))
        self.label_2.setText(_translate("MainWindow", "印章名称"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">印章类型</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">印章形状</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">印章尺寸</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">印章材质</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">印章字体</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">印章用途</p></body></html>"))
        self.lb_time_s.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">启用时间</p></body></html>"))
        self.lb_original_dept.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">原保管单位</p></body></html>"))
        self.lb_keeper.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">保管人</p></body></html>"))
        self.lb_time_e.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">停用时间</p></body></html>"))
        self.lb_keep_dept.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">停用后保管单位</p></body></html>"))
        self.lb_saved.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">归档与否</p></body></html>"))
        self.pb_new.setText(_translate("MainWindow", "新建"))
        self.pb_add.setText(_translate("MainWindow", "添加"))
        self.pb_change.setText(_translate("MainWindow", "修改"))
        self.pb_del.setText(_translate("MainWindow", "删除"))
    def click_pb_new(self):
        self.rpt_deact.setEnabled(True)
        self.rpt_disabled.setEnabled(True)
        self.rpt_enabled.setEnabled(True)
        self.rpt_maint.setEnabled(True)
        self.line_SealName.setEnabled(True)
        datatable=['SealType','SealShape','Sealsize','Sealmaterial','Sealfont','Sealuse']
        for (table,cb) in zip(datatable,self.cb_group):
            cb.clear()
            sql="select standname from "+table
            self.cursor.execute(sql)
            result=self.cursor.fetchall()
            if len(result)==0:
                result.append('无')
            t=list()
            for row in result:
                t.append(row[0])
            cb.addItems(t)
    def btnstate(self,btn):
    #输出按钮1与按钮2的状态，选中还是没选中
        if btn.text()=="停用":
            if btn.isChecked()==True:
                for cb in self.deact_cb_group:
                    cb.setVisible(True)
                    cb.setEnabled(True)

                for lb in self.deact_lb_group:
                    lb.setVisible(True)
                self.state = btn.text()
            else:
                for cb in self.deact_cb_group:
                    cb.setVisible(False)
                    cb.setEnabled(False)

                for lb in self.deact_lb_group:
                    lb.setVisible(False)

    def table_add(self):
        """获取B区数据存入数据库，显示在A区"""
        self.rpt_deact.setEnabled(False)
        self.rpt_disabled.setEnabled(False)
        self.rpt_enabled.setEnabled(False)
        self.rpt_maint.setEnabled(False)
        self.line_SealName.setEnabled(False)
        for cb in self.cb_group:
            cb.clear()
        #####
        #若数据已经存在则添加失败，弹出已添加该标准
        ##############
        #在B表上添加一行
        n=1
        #p=database.xxx  连接数据库获得历史创建过的印章熟练
        code = "P"+str(n).zfill(6)
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        item_seal_name = QTableWidgetItem(self.line_SealName.text())
        item_seal_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item_code = QTableWidgetItem(code)
        item_code.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.tableWidget.setItem(rowPosition, 0, item_code)
        self.tableWidget.setItem(rowPosition, 1, item_seal_name)

        self.line_SealName.clear()
        self.pb_add.setEnabled(False)
        self.pb_new.setEnabled(True)

        QtWidgets.QMessageBox.information(self.Form, 'Message',
                                          "添加成功!")
    def table_slot(self):
        """获取表中的信息显示在右边"""
        row_select = self.tableWidget.selectedItems()
        if len(row_select) == 0:
            return
        self.pb_change.setEnabled(True)
        self.pb_del.setEnabled(True)

        """连接数据库
        seal_code = self.tableWidget.item(row_select[], 0).text()
        # data_set = database.get_data(seal_code) #这里可能需要传入印章状态的参数
        if data_set.state == "停用":
            self.rpt_deact.setChecked(True) #重置印章状态
        elif xxxxx
    
        if self.state == "停用"：
            for edit in self.deact_group:
                try:
                    edit.setText(data[edit.text])
                except:
                    edit.setDate(data[edit.text])
        """
        #测试
        self.rpt_deact.setChecked(True)
        self.setup_combo_box_all()
        self.cb_type.setCurrentText("湖南省")

    def table_del(self):
        row_select = self.tableWidget.selectedItems()
        if len(row_select) == 0:
            return

        row = row_select[0].row()
        self.tableWidget.removeRow(row)
        # 以下插入从数据库中删除数据
        '''
        eg. delete from {table} where id = "id"
        '''
        self.pb_change.setEnabled(False)
        self.pb_del.setEnabled(False)
        QtWidgets.QMessageBox.information(self.Form, 'Message',
                                          "删除成功!")

    def table_change(self):
        """
        选择A区域的某行进行修改
        """
        row_select = self.tableWidget.selectedItems()
        if len(row_select) == 0:
            return
        seal_name = self.line_SealName.text()
        row = row_select[0].row()

        item_seal_name = QTableWidgetItem(seal_name)
        item_seal_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.tableWidget.setItem(row, 1, item_seal_name)
        """
        连接数据库修改数据
        data = database.get_data(self.tableWidget.item(row,0).text())
        """

        self.pb_change.setEnabled(False)
        self.pb_del.setEnabled(False)

        QtWidgets.QMessageBox.information(self.Form, 'Message',
                                          "修改成功!")
    def innitial(self,u):
        self.data=u
if __name__ == "__main__":
    app = QApplication(sys.argv)
    handover = QMainWindow()
    ui_handover = Ui_SealManager()
    ui_handover.setupUi(handover)
    handover.show()
    sys.exit(app.exec_())
