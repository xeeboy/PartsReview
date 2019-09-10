# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chgpwd.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chgpwd(object):
    def setupUi(self, chgpwd):
        chgpwd.setObjectName("chgpwd")
        chgpwd.setWindowModality(QtCore.Qt.WindowModal)
        chgpwd.resize(423, 151)
        chgpwd.setMinimumSize(QtCore.QSize(423, 151))
        chgpwd.setMaximumSize(QtCore.QSize(423, 151))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        chgpwd.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/password128px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        chgpwd.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(chgpwd)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 40, 281, 85))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.line_pwd_again = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)
        self.line_pwd_again.setFont(font)
        self.line_pwd_again.setMaxLength(20)
        self.line_pwd_again.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pwd_again.setClearButtonEnabled(True)
        self.line_pwd_again.setObjectName("line_pwd_again")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_pwd_again)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.line_pwd_one = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)
        self.line_pwd_one.setFont(font)
        self.line_pwd_one.setMaxLength(20)
        self.line_pwd_one.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pwd_one.setClearButtonEnabled(True)
        self.line_pwd_one.setObjectName("line_pwd_one")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_pwd_one)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.label_3 = QtWidgets.QLabel(chgpwd)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 131, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icons/password128px.ico"))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(chgpwd)
        self.buttonBox.accepted.connect(chgpwd.accept)
        self.buttonBox.rejected.connect(chgpwd.reject)
        QtCore.QMetaObject.connectSlotsByName(chgpwd)
        chgpwd.setTabOrder(self.line_pwd_one, self.line_pwd_again)

    def retranslateUi(self, chgpwd):
        _translate = QtCore.QCoreApplication.translate
        chgpwd.setWindowTitle(_translate("chgpwd", "更改密码"))
        self.label.setText(_translate("chgpwd", "New Password:"))
        self.label_2.setText(_translate("chgpwd", "Enter again:"))


