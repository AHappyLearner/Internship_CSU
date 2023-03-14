from PyQt5 import QtCore, QtWidgets
from qtpy.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView

class Ui_SealStandards(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget_B = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_B.setObjectName("tableWidget_B")
        self.tableWidget_B.setColumnCount(2)
        self.tableWidget_B.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_B.setHorizontalHeaderItem(1, item)
        self.gridLayout_3.addWidget(self.tableWidget_B, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.tableWidget_A = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_A.setObjectName("tableWidget_A")
        self.tableWidget_A.setColumnCount(2)
        self.tableWidget_A.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_A.setHorizontalHeaderItem(0, item)
        self.tableWidget_A.horizontalHeader().setVisible(False)
        self.tableWidget_A.horizontalHeader().setDefaultSectionSize(147)
        self.tableWidget_A.verticalHeader().setVisible(True)
        self.tableWidget_A.verticalHeader().setHighlightSections(True)
        self.tableWidget_A.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_3.addWidget(self.tableWidget_A)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 0, 3, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_stand_name = QtWidgets.QLineEdit(self.centralwidget)
        self.line_stand_name.setEnabled(False)
        self.line_stand_name.setObjectName("line_stand_name")
        self.verticalLayout.addWidget(self.line_stand_name)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line_remark = QtWidgets.QTextEdit(self.centralwidget)
        self.line_remark.setEnabled(False)
        self.line_remark.setObjectName("line_remark")
        self.verticalLayout.addWidget(self.line_remark)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pt_del = QtWidgets.QPushButton(self.centralwidget)
        self.pt_del.setEnabled(False)
        self.pt_del.setObjectName("pt_del")
        self.gridLayout.addWidget(self.pt_del, 1, 1, 1, 1)
        self.pt_change = QtWidgets.QPushButton(self.centralwidget)
        self.pt_change.setEnabled(False)
        self.pt_change.setObjectName("pt_change")
        self.gridLayout.addWidget(self.pt_change, 1, 0, 1, 1)
        self.pt_new = QtWidgets.QPushButton(self.centralwidget)
        self.pt_new.setObjectName("pt_new")
        self.gridLayout.addWidget(self.pt_new, 0, 0, 1, 1)
        self.pt_add = QtWidgets.QPushButton(self.centralwidget)
        self.pt_add.setEnabled(False)
        self.pt_add.setObjectName("pt_add")
        self.gridLayout.addWidget(self.pt_add, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 2, 3)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 1, 1, 1)
        self.horizontalLayout_8.addLayout(self.gridLayout_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cursor = self.data.cursor
        self.pt_new.clicked['bool'].connect(self.table_new)
        self.pt_add.clicked['bool'].connect(lambda:self.table_add(MainWindow))
        self.pt_change.clicked['bool'].connect(self.table_change)
        self.pt_del.clicked['bool'].connect(self.table_del)
        self.tableWidget_A.clicked.connect(self.tableA_slot)
        self.tableWidget_B.clicked.connect(self.tableB_slot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tableWidget_A.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
        self.tableWidget_A.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_B.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
        self.tableWidget_B.setSelectionMode(QAbstractItemView.SingleSelection)

        self.datatable=['SealType','SealShape','Sealsize','Sealmaterial','Sealfont','Sealuse',
                        'sealcurreason','sealfixreason','sealDeactivatereason','sealHandoverreason',
                        'FileTitleManage','sealname','deptname']
        self.tableWidget_A.selectRow(4)
        self.tableA_slot()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "印章标准管理"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">印章标准管理</span></p></body></html>"))

        item = self.tableWidget_B.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "标准名称"))
        item = self.tableWidget_B.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "备注"))

        self.pt_change.setText(_translate("MainWindow", "修改"))
        self.pt_add.setText(_translate("MainWindow", "添加"))
        self.pt_del.setText(_translate("MainWindow", "删除"))
        self.pt_new.setText(_translate("MainWindow", "新建"))
        self.label.setText(_translate("MainWindow", "标准名称"))
        self.label_2.setText(_translate("MainWindow", "备注"))
        self.label_4.setText(_translate("MainWindow", "标准类型"))
        self.label_6.setText(_translate("MainWindow", "备注"))

        #添加备注信息
        item_SealType = QTableWidgetItem("印章类型")
        item_SealType_rm = QTableWidgetItem("")
        item_SealType.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置物件的状态为只可被选择（未设置可编辑）

        item_SealShape = QTableWidgetItem("印章形状")
        item_SealShape_rm = QTableWidgetItem("")
        item_SealShape.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        #尺寸
        item_SealSize = QTableWidgetItem("印章尺寸")
        item_SealSize_rm = QTableWidgetItem("")
        item_SealSize.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        item_SealMaterial = QTableWidgetItem("印章材质")
        item_SealMaterial_rm = QTableWidgetItem("")
        item_SealMaterial.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        #印章字体
        item_SealFont = QTableWidgetItem("印章字体")
        item_SealFont_rm = QTableWidgetItem("")
        item_SealFont.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        item_SealUse = QTableWidgetItem("印章用途")
        item_SealUse_rm = QTableWidgetItem("")
        item_SealUse.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        item_CurveReason = QTableWidgetItem("印章刻制原因")
        item_CurveReason_rm = QTableWidgetItem("")
        item_CurveReason.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        item_MaintReason = QTableWidgetItem("印章维修原因")
        item_MaintReason_rm = QTableWidgetItem("")
        item_MaintReason.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置物件的状态为只可被选择

        #停用原因
        item_DeactReason = QTableWidgetItem("印章停用原因")
        item_DeactReason_rm = QTableWidgetItem("")
        item_DeactReason.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        #交接原因
        item_TransReason = QTableWidgetItem("印章交接原因")
        item_TransReason_rm = QTableWidgetItem("")
        item_TransReason.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        item_FileTitle = QTableWidgetItem("文件标题管理")
        item_FileTitle_rm = QTableWidgetItem("")
        item_FileTitle.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        item_sealname=QTableWidgetItem("印章名称管理")
        item_sealname_rm = QTableWidgetItem("")
        item_sealname.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        item_dept=QTableWidgetItem("部门管理")
        item_dept_rm = QTableWidgetItem("")
        item_dept.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        #self.tableWidget_A.insertRow(13)
        self.tableWidget_A.setItem(0, 0, item_SealType)
        self.tableWidget_A.setItem(1, 0, item_SealShape)
        self.tableWidget_A.setItem(2, 0, item_SealSize)
        self.tableWidget_A.setItem(3, 0, item_SealMaterial)
        self.tableWidget_A.setItem(4, 0, item_SealFont)
        self.tableWidget_A.setItem(5, 0, item_SealUse)
        self.tableWidget_A.setItem(6, 0, item_CurveReason)
        self.tableWidget_A.setItem(7, 0, item_MaintReason)
        self.tableWidget_A.setItem(8, 0, item_DeactReason)
        self.tableWidget_A.setItem(9, 0, item_TransReason)
        self.tableWidget_A.setItem(10, 0, item_FileTitle)
        self.tableWidget_A.setItem(11,0,item_sealname)
        self.tableWidget_A.setItem(12, 0, item_dept)

        self.tableWidget_A.setItem(0, 1, item_SealType_rm)
        self.tableWidget_A.setItem(1, 1, item_SealShape_rm)
        self.tableWidget_A.setItem(2, 1, item_SealSize_rm)
        self.tableWidget_A.setItem(3, 1, item_SealMaterial_rm)
        self.tableWidget_A.setItem(4, 1, item_SealFont_rm)
        self.tableWidget_A.setItem(5, 1, item_SealUse_rm)
        self.tableWidget_A.setItem(6, 1, item_CurveReason_rm)
        self.tableWidget_A.setItem(7, 1, item_MaintReason_rm)
        self.tableWidget_A.setItem(8, 1, item_DeactReason_rm)
        self.tableWidget_A.setItem(9, 1, item_TransReason_rm)
        self.tableWidget_A.setItem(10, 1, item_FileTitle_rm)
        self.tableWidget_A.setItem(11, 1, item_sealname_rm)
        self.tableWidget_A.setItem(12, 1, item_dept_rm)

    def tableB_slot(self):
        """
        点击表B后的反应
        """
        row_select = self.tableWidget_B.selectedItems()
        if len(row_select) == 0:
            return
        self.pt_del.setEnabled(True)
        self.pt_change.setEnabled(True)
        self.pt_new.setEnabled(False)
        self.pt_add.setEnabled(False)
        row_index = row_select[0].row()
        self.line_stand_name.setText(self.tableWidget_B.item(row_index, 0).text())
        self.txt=self.line_stand_name.text()
        self.line_remark.setText(self.tableWidget_B.item(row_index, 1).text())
        self.line_stand_name.setEnabled(True)
        self.line_remark.setEnabled(True)

    def table_new(self):
        """
        点击新建按钮后触发此函数
        """
        row_select = self.tableWidget_A.selectedItems()
        if len(row_select) == 0:
            return
        self.pt_add.setEnabled(True)
        self.pt_new.setEnabled(False)
        self.line_stand_name.setEnabled(True)
        self.line_remark.setEnabled(True)

    def table_add(self,Form):
        """获取self.line_stand_name，self.line_remark存入数据库"""
        row_select = self.tableWidget_A.selectedItems()
        index=self.tableWidget_A.currentRow()
        if len(row_select) == 0:
            return
        table = self.datatable[index]
        try:
            sql="insert into "+table+" values("+repr(self.line_stand_name.text())+","
            sql=sql+repr(self.line_remark.toPlainText())+")"
            self.cursor.execute(sql)
            self.data.conn.commit()
            self.cursor.execute("select standname from "+table)
            result=self.cursor.fetchall()
            num=len(result)
            sealnum="p"+str(num).zfill(5)
            sql="insert into seal values("+repr(sealnum)+","+repr(self.line_stand_name.text())+")"
            if index==11:
                self.cursor.execute(sql)
                self.data.conn.commit()

            self.data.conn.commit()
            # 清楚文本框
            self.line_stand_name.clear()
            self.line_remark.clear()
            self.line_stand_name.setEnabled(False)
            self.line_remark.setEnabled(False)
            self.pt_add.setEnabled(False)
            self.pt_new.setEnabled(True)
            # 显示添加后表的数据
            self.tableA_slot()
        except:
            QtWidgets.QMessageBox.information(Form, 'Message',
                                              "insert error,standard is already exit!")

    def tableA_slot(self):
        self.pt_new.setEnabled(True)
        self.pt_add.setEnabled(False)
        row_select = self.tableWidget_A.selectedItems()
        index=self.tableWidget_A.currentRow()
        if len(row_select) == 0:
            return
        """点击A区某行更新B区中的表格"""
        count=self.tableWidget_B.rowCount()
        self.tableWidget_B.clearContents()
        for i in range(0,count+1):
            self.tableWidget_B.removeRow(0)
        table = self.datatable[index]
        sql="select * from "+table
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        for row in data:
            rowPosition = self.tableWidget_B.rowCount()
            self.tableWidget_B.insertRow(rowPosition)
            item_stand_name = QTableWidgetItem(row[0])
            item_stand_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item_remark = QTableWidgetItem(row[1])
            item_remark.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.tableWidget_B.setItem(rowPosition, 0, item_stand_name)
            self.tableWidget_B.setItem(rowPosition, 1, item_remark)

        self.pt_change.setEnabled(False)
        self.pt_del.setEnabled(False)
        self.line_stand_name.clear()
        self.line_remark.clear()
        self.line_stand_name.setEnabled(False)
        self.line_remark.setEnabled(False)

    def table_change(self):
        """
        选择B区域的某行进行修改
        """
        row_select = self.tableWidget_B.selectedItems()
        if len(row_select) == 0:
            return
        stand_name = self.line_stand_name.text()
        remark = QTableWidgetItem(str(self.line_remark.toPlainText()))
        row = row_select[0].row()

        item_stand_name = QTableWidgetItem(stand_name)
        item_stand_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item_remark = QTableWidgetItem(remark)
        item_remark.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.tableWidget_B.setItem(row, 0, item_stand_name)
        self.tableWidget_B.setItem(row, 1, item_remark)
        #连接数据库修改数据
        index=self.tableWidget_A.currentRow()
        table=self.datatable[index]
        sql="update "+table+" set standname="+repr(stand_name)+","
        sql=sql + "info="+repr(self.line_remark.toPlainText())+" where standname="+repr(stand_name)
        sql2="select * from "+table+" where standname="+repr(stand_name)
        self.cursor.execute(sql2)
        result=self.cursor.fetchall()
        if len(result)==0:
            sql = "insert into " + table + " values(" + repr(self.line_stand_name.text()) + ","
            sql = sql + repr(self.line_remark.toPlainText()) + ")"
            self.cursor.execute("delete from "+table+" where standname="+repr(self.txt))
        try:
            self.cursor.execute(sql)
            self.data.conn.commit()

            self.pt_change.setEnabled(False)
            self.pt_del.setEnabled(False)
            self.line_stand_name.setEnabled(False)
            self.line_remark.setEnabled(False)
            self.line_remark.clear()
            self.line_stand_name.clear()
        except:
            QtWidgets.QMessageBox.information(self.Form, 'Message',
                                              "insert error,standard is already exit!")

    def table_del(self):
        row_select = self.tableWidget_B.selectedItems()
        if len(row_select) == 0:
            return

        # 以下插入从数据库中删除数据
        index = self.tableWidget_A.currentRow()
        table = self.datatable[index]
        sql = "delete from " + table +" where standname=" + repr(self.line_stand_name.text())
        self.cursor.execute(sql)
        sql = "delete from seal where sealname=" + repr(self.line_stand_name.text())
        self.cursor.execute(sql)
        self.data.conn.commit()
        self.tableA_slot()
        self.pt_change.setEnabled(False)
        self.pt_del.setEnabled(False)
        self.line_stand_name.setEnabled(False)
        self.line_remark.setEnabled(False)
        self.line_remark.clear()
        self.line_stand_name.clear()

        self.data.conn.commit()

    def innitial(self,u):
        self.data=u
