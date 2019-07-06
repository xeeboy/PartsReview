# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_item.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_plot_item(object):
    def setupUi(self, plot_item):
        plot_item.setObjectName("plot_item")
        plot_item.resize(277, 353)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        plot_item.setWindowIcon(icon)
        self.btn_isok = QtWidgets.QDialogButtonBox(plot_item)
        self.btn_isok.setGeometry(QtCore.QRect(50, 310, 171, 32))
        self.btn_isok.setOrientation(QtCore.Qt.Horizontal)
        self.btn_isok.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_isok.setObjectName("btn_isok")
        self.groupBox = QtWidgets.QGroupBox(plot_item)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 201, 271))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout.addWidget(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout.addWidget(self.radioButton_9)

        self.retranslateUi(plot_item)
        self.btn_isok.accepted.connect(plot_item.accept)
        self.btn_isok.rejected.connect(plot_item.reject)
        QtCore.QMetaObject.connectSlotsByName(plot_item)

    def retranslateUi(self, plot_item):
        _translate = QtCore.QCoreApplication.translate
        plot_item.setWindowTitle(_translate("plot_item", "选择项目"))
        self.groupBox.setTitle(_translate("plot_item", "选择一项生成折线图"))
        self.radioButton.setText(_translate("plot_item", "密度"))
        self.radioButton_2.setText(_translate("plot_item", "拉伸强度"))
        self.radioButton_3.setText(_translate("plot_item", "断裂伸长率"))
        self.radioButton_4.setText(_translate("plot_item", "断裂根数"))
        self.radioButton_5.setText(_translate("plot_item", "体积电阻率"))
        self.radioButton_6.setText(_translate("plot_item", "硬度"))
        self.radioButton_7.setText(_translate("plot_item", "200℃热稳定时间"))
        self.radioButton_8.setText(_translate("plot_item", "介电强度"))
        self.radioButton_9.setText(_translate("plot_item", "氧指数"))


