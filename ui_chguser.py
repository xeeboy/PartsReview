# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chguser.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chguser(object):
    def setupUi(self, chguser):
        chguser.setObjectName("chguser")
        chguser.setWindowModality(QtCore.Qt.WindowModal)
        chguser.resize(292, 179)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        chguser.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/partner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        chguser.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(chguser)
        self.buttonBox.setGeometry(QtCore.QRect(120, 140, 156, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(chguser)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 251, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.line_chg_pwd = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_chg_pwd.setMaxLength(20)
        self.line_chg_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_chg_pwd.setClearButtonEnabled(True)
        self.line_chg_pwd.setObjectName("line_chg_pwd")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_chg_pwd)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.line_chg_user = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_chg_user.setMaxLength(20)
        self.line_chg_user.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_chg_user.setClearButtonEnabled(True)
        self.line_chg_user.setObjectName("line_chg_user")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_chg_user)

        self.retranslateUi(chguser)
        self.buttonBox.accepted.connect(chguser.accept)
        self.buttonBox.rejected.connect(chguser.reject)
        QtCore.QMetaObject.connectSlotsByName(chguser)
        chguser.setTabOrder(self.line_chg_user, self.line_chg_pwd)

    def retranslateUi(self, chguser):
        _translate = QtCore.QCoreApplication.translate
        chguser.setWindowTitle(_translate("chguser", "更换用户"))
        self.label.setText(_translate("chguser", "请输入用户名："))
        self.label_2.setText(_translate("chguser", "请输入密码："))


