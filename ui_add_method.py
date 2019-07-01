# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_method.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_method(object):
    def setupUi(self, add_method):
        add_method.setObjectName("add_method")
        add_method.resize(456, 262)
        add_method.setMaximumSize(QtCore.QSize(456, 262))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/input_tablet_32px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_method.setWindowIcon(icon)
        self.formLayoutWidget = QtWidgets.QWidget(add_method)
        self.formLayoutWidget.setGeometry(QtCore.QRect(170, 30, 271, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.line_deal_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_deal_id.setEnabled(False)
        self.line_deal_id.setObjectName("line_deal_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_deal_id)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.line_unpass_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_unpass_id.setEnabled(False)
        self.line_unpass_id.setObjectName("line_unpass_id")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_unpass_id)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.date_deal = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.date_deal.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 6, 30), QtCore.QTime(0, 0, 0)))
        self.date_deal.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2017, 9, 14), QtCore.QTime(0, 0, 0)))
        self.date_deal.setCalendarPopup(True)
        self.date_deal.setDate(QtCore.QDate(2019, 6, 30))
        self.date_deal.setObjectName("date_deal")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.date_deal)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txt_deal_method = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.txt_deal_method.setObjectName("txt_deal_method")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_deal_method)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.line_deal_qty = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_deal_qty.setObjectName("line_deal_qty")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_deal_qty)
        self.btn_save_method = QtWidgets.QPushButton(add_method)
        self.btn_save_method.setGeometry(QtCore.QRect(370, 230, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/confirm128px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save_method.setIcon(icon1)
        self.btn_save_method.setObjectName("btn_save_method")
        self.label_5 = QtWidgets.QLabel(add_method)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 151, 151))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("icons/find.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(add_method)
        QtCore.QMetaObject.connectSlotsByName(add_method)
        add_method.setTabOrder(self.date_deal, self.line_deal_qty)
        add_method.setTabOrder(self.line_deal_qty, self.txt_deal_method)
        add_method.setTabOrder(self.txt_deal_method, self.btn_save_method)
        add_method.setTabOrder(self.btn_save_method, self.line_deal_id)
        add_method.setTabOrder(self.line_deal_id, self.line_unpass_id)

    def retranslateUi(self, add_method):
        _translate = QtCore.QCoreApplication.translate
        add_method.setWindowTitle(_translate("add_method", "添加处置方式"))
        self.label.setText(_translate("add_method", "序号"))
        self.label_2.setText(_translate("add_method", "不合格品ID"))
        self.label_4.setText(_translate("add_method", "处理日期"))
        self.label_3.setText(_translate("add_method", "处理措施"))
        self.label_6.setText(_translate("add_method", "处理数量Kg"))
        self.btn_save_method.setText(_translate("add_method", "添加"))


