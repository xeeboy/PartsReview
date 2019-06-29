# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(761, 552)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(761, 552))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/parameterreview_32px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_ongoing = QtWidgets.QWidget()
        self.tab_ongoing.setObjectName("tab_ongoing")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_ongoing)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.tab_ongoing)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 7, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_ongoing)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)
        self.unpassname = QtWidgets.QLineEdit(self.tab_ongoing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unpassname.sizePolicy().hasHeightForWidth())
        self.unpassname.setSizePolicy(sizePolicy)
        self.unpassname.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.unpassname.setFont(font)
        self.unpassname.setReadOnly(True)
        self.unpassname.setObjectName("unpassname")
        self.gridLayout.addWidget(self.unpassname, 1, 5, 1, 1)
        self.batch = QtWidgets.QLineEdit(self.tab_ongoing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batch.sizePolicy().hasHeightForWidth())
        self.batch.setSizePolicy(sizePolicy)
        self.batch.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.batch.setFont(font)
        self.batch.setReadOnly(True)
        self.batch.setObjectName("batch")
        self.gridLayout.addWidget(self.batch, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_ongoing)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.prodate = QtWidgets.QLineEdit(self.tab_ongoing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prodate.sizePolicy().hasHeightForWidth())
        self.prodate.setSizePolicy(sizePolicy)
        self.prodate.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.prodate.setFont(font)
        self.prodate.setReadOnly(True)
        self.prodate.setObjectName("prodate")
        self.gridLayout.addWidget(self.prodate, 0, 9, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_ongoing)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.unpasstype = QtWidgets.QLineEdit(self.tab_ongoing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unpasstype.sizePolicy().hasHeightForWidth())
        self.unpasstype.setSizePolicy(sizePolicy)
        self.unpasstype.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.unpasstype.setFont(font)
        self.unpasstype.setReadOnly(True)
        self.unpasstype.setObjectName("unpasstype")
        self.gridLayout.addWidget(self.unpasstype, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_ongoing)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 7, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_ongoing)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)
        self.unpassqty = QtWidgets.QLineEdit(self.tab_ongoing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unpassqty.sizePolicy().hasHeightForWidth())
        self.unpassqty.setSizePolicy(sizePolicy)
        self.unpassqty.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.unpassqty.setFont(font)
        self.unpassqty.setReadOnly(True)
        self.unpassqty.setObjectName("unpassqty")
        self.gridLayout.addWidget(self.unpassqty, 1, 9, 1, 1)
        self.ID = QtWidgets.QLineEdit(self.tab_ongoing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ID.sizePolicy().hasHeightForWidth())
        self.ID.setSizePolicy(sizePolicy)
        self.ID.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ID.setFont(font)
        self.ID.setReadOnly(True)
        self.ID.setObjectName("ID")
        self.gridLayout.addWidget(self.ID, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 10, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.tab_ongoing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.formLayout_2)
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.describe = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setItalic(False)
        self.describe.setFont(font)
        self.describe.setReadOnly(True)
        self.describe.setObjectName("describe")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.describe)
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.result = QtWidgets.QTextEdit(self.frame)
        self.result.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.result)
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.precaution = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.precaution.setFont(font)
        self.precaution.setObjectName("precaution")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.precaution)
        self.label_17 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.person = QtWidgets.QLabel(self.frame)
        self.person.setText("")
        self.person.setObjectName("person")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.person)
        self.pre_check = QtWidgets.QCheckBox(self.frame)
        self.pre_check.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pre_check.setChecked(False)
        self.pre_check.setObjectName("pre_check")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.pre_check)
        self.parts = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parts.sizePolicy().hasHeightForWidth())
        self.parts.setSizePolicy(sizePolicy)
        self.parts.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.parts.setFont(font)
        self.parts.setClearButtonEnabled(False)
        self.parts.setObjectName("parts")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.parts)
        self.btn_slparts = QtWidgets.QPushButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/user.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_slparts.setIcon(icon1)
        self.btn_slparts.setObjectName("btn_slparts")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.btn_slparts)
        self.pre_time = QtWidgets.QLabel(self.frame)
        self.pre_time.setText("")
        self.pre_time.setObjectName("pre_time")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.pre_time)
        self.label_6 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.btn_save = QtWidgets.QPushButton(self.frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/Save_32px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon2)
        self.btn_save.setObjectName("btn_save")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.btn_save)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(13, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(12, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        self.correctiveaciton = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.correctiveaciton.setFont(font)
        self.correctiveaciton.setObjectName("correctiveaciton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.correctiveaciton)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.tab_ongoing)
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_11.setClearButtonEnabled(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_2.addWidget(self.lineEdit_11)
        self.btn_search = QtWidgets.QPushButton(self.frame_3)
        self.btn_search.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/search.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon3)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_2.addWidget(self.btn_search)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.tbl_unpass = QtWidgets.QTableView(self.frame_2)
        self.tbl_unpass.setObjectName("tbl_unpass")
        self.verticalLayout_5.addWidget(self.tbl_unpass)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/dir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_ongoing, icon4, "")
        self.tab_onpreving = QtWidgets.QWidget()
        self.tab_onpreving.setObjectName("tab_onpreving")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_onpreving)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.tab_onpreving)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pre_tbl_view = QtWidgets.QTableView(self.frame_5)
        self.pre_tbl_view.setObjectName("pre_tbl_view")
        self.verticalLayout_8.addWidget(self.pre_tbl_view)
        self.txt_pre_info = QtWidgets.QTextEdit(self.frame_5)
        self.txt_pre_info.setObjectName("txt_pre_info")
        self.verticalLayout_8.addWidget(self.txt_pre_info)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.btn_sign_pre = QtWidgets.QPushButton(self.frame_5)
        self.btn_sign_pre.setObjectName("btn_sign_pre")
        self.horizontalLayout_4.addWidget(self.btn_sign_pre)
        self.btn_save_pre = QtWidgets.QPushButton(self.frame_5)
        self.btn_save_pre.setObjectName("btn_save_pre")
        self.horizontalLayout_4.addWidget(self.btn_save_pre)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8.setStretch(0, 6)
        self.verticalLayout_8.setStretch(1, 1)
        self.horizontalLayout_3.addWidget(self.frame_5)
        spacerItem9 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.frame_4 = QtWidgets.QFrame(self.tab_onpreving)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setLineWidth(0)
        self.frame_4.setMidLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setObjectName("label_22")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.pre_describle = QtWidgets.QTextEdit(self.frame_4)
        self.pre_describle.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_describle.setReadOnly(True)
        self.pre_describle.setObjectName("pre_describle")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pre_describle)
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.pre_result = QtWidgets.QTextEdit(self.frame_4)
        self.pre_result.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_result.setReadOnly(True)
        self.pre_result.setObjectName("pre_result")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pre_result)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.pre_correctiveation = QtWidgets.QTextEdit(self.frame_4)
        self.pre_correctiveation.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_correctiveation.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pre_correctiveation.setReadOnly(True)
        self.pre_correctiveation.setObjectName("pre_correctiveation")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pre_correctiveation)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.pre_precaution = QtWidgets.QTextEdit(self.frame_4)
        self.pre_precaution.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_precaution.setReadOnly(True)
        self.pre_precaution.setObjectName("pre_precaution")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pre_precaution)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.pre_tec_idea = QtWidgets.QTextEdit(self.frame_4)
        self.pre_tec_idea.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_tec_idea.setReadOnly(True)
        self.pre_tec_idea.setObjectName("pre_tec_idea")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pre_tec_idea)
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.pre_pro_idea = QtWidgets.QTextEdit(self.frame_4)
        self.pre_pro_idea.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_pro_idea.setReadOnly(True)
        self.pre_pro_idea.setObjectName("pre_pro_idea")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pre_pro_idea)
        self.label_19 = QtWidgets.QLabel(self.frame_4)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.pre_qa_idea = QtWidgets.QTextEdit(self.frame_4)
        self.pre_qa_idea.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_qa_idea.setReadOnly(True)
        self.pre_qa_idea.setObjectName("pre_qa_idea")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pre_qa_idea)
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setObjectName("label_20")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.pre_tec_support_idea = QtWidgets.QTextEdit(self.frame_4)
        self.pre_tec_support_idea.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_tec_support_idea.setReadOnly(True)
        self.pre_tec_support_idea.setObjectName("pre_tec_support_idea")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pre_tec_support_idea)
        self.verticalLayout_7.addLayout(self.formLayout_4)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.tab_onpreving)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_6.setLineWidth(0)
        self.frame_6.setMidLineWidth(1)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_29 = QtWidgets.QLabel(self.frame_6)
        self.label_29.setObjectName("label_29")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.lbl_rev_parts_need = QtWidgets.QLabel(self.frame_6)
        self.lbl_rev_parts_need.setText("")
        self.lbl_rev_parts_need.setObjectName("lbl_rev_parts_need")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbl_rev_parts_need)
        spacerItem10 = QtWidgets.QSpacerItem(19, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem10)
        self.label_21 = QtWidgets.QLabel(self.frame_6)
        self.label_21.setObjectName("label_21")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.pre_info_purchase = QtWidgets.QTextEdit(self.frame_6)
        self.pre_info_purchase.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_info_purchase.setReadOnly(True)
        self.pre_info_purchase.setObjectName("pre_info_purchase")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pre_info_purchase)
        self.label_23 = QtWidgets.QLabel(self.frame_6)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.pre_info_produce = QtWidgets.QTextEdit(self.frame_6)
        self.pre_info_produce.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_info_produce.setReadOnly(True)
        self.pre_info_produce.setObjectName("pre_info_produce")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pre_info_produce)
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.pre_info_process = QtWidgets.QTextEdit(self.frame_6)
        self.pre_info_process.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_info_process.setReadOnly(True)
        self.pre_info_process.setObjectName("pre_info_process")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pre_info_process)
        self.label_25 = QtWidgets.QLabel(self.frame_6)
        self.label_25.setObjectName("label_25")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.pre_info_logistics = QtWidgets.QTextEdit(self.frame_6)
        self.pre_info_logistics.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_info_logistics.setReadOnly(True)
        self.pre_info_logistics.setObjectName("pre_info_logistics")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pre_info_logistics)
        self.label_26 = QtWidgets.QLabel(self.frame_6)
        self.label_26.setObjectName("label_26")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.pre_info_tec = QtWidgets.QTextEdit(self.frame_6)
        self.pre_info_tec.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_info_tec.setReadOnly(True)
        self.pre_info_tec.setObjectName("pre_info_tec")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pre_info_tec)
        self.label_27 = QtWidgets.QLabel(self.frame_6)
        self.label_27.setObjectName("label_27")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.pre_info_qa = QtWidgets.QTextEdit(self.frame_6)
        self.pre_info_qa.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_info_qa.setReadOnly(True)
        self.pre_info_qa.setObjectName("pre_info_qa")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pre_info_qa)
        self.label_28 = QtWidgets.QLabel(self.frame_6)
        self.label_28.setObjectName("label_28")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.pre_info_general = QtWidgets.QTextEdit(self.frame_6)
        self.pre_info_general.setFrameShape(QtWidgets.QFrame.Box)
        self.pre_info_general.setReadOnly(True)
        self.pre_info_general.setObjectName("pre_info_general")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pre_info_general)
        self.verticalLayout_9.addLayout(self.formLayout_3)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(2, 3)
        self.horizontalLayout_3.setStretch(3, 3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_onpreving, icon5, "")
        self.tab_following = QtWidgets.QWidget()
        self.tab_following.setObjectName("tab_following")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/gps_navigation_32px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_following, icon6, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.act_chgpwd = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/password32px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_chgpwd.setIcon(icon7)
        self.act_chgpwd.setObjectName("act_chgpwd")
        self.act_chguser = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/user32px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_chguser.setIcon(icon8)
        self.act_chguser.setObjectName("act_chguser")
        self.act_quit = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/quit128px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_quit.setIcon(icon9)
        self.act_quit.setObjectName("act_quit")
        self.act_about = QtWidgets.QAction(MainWindow)
        self.act_about.setIcon(icon4)
        self.act_about.setObjectName("act_about")
        self.menu.addAction(self.act_chgpwd)
        self.menu.addAction(self.act_chguser)
        self.menu.addSeparator()
        self.menu.addAction(self.act_quit)
        self.menuHelp.addAction(self.act_about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.act_quit.triggered.connect(MainWindow.close)
        self.lineEdit_11.returnPressed.connect(self.btn_search.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.result, self.precaution)
        MainWindow.setTabOrder(self.precaution, self.lineEdit_11)
        MainWindow.setTabOrder(self.lineEdit_11, self.btn_search)
        MainWindow.setTabOrder(self.btn_search, self.pre_check)
        MainWindow.setTabOrder(self.pre_check, self.describe)
        MainWindow.setTabOrder(self.describe, self.tbl_unpass)
        MainWindow.setTabOrder(self.tbl_unpass, self.unpassname)
        MainWindow.setTabOrder(self.unpassname, self.batch)
        MainWindow.setTabOrder(self.batch, self.prodate)
        MainWindow.setTabOrder(self.prodate, self.unpasstype)
        MainWindow.setTabOrder(self.unpasstype, self.unpassqty)
        MainWindow.setTabOrder(self.unpassqty, self.ID)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "不合格品评审系统"))
        self.label_11.setText(_translate("MainWindow", "数量Kg"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_4.setText(_translate("MainWindow", "不良品种类"))
        self.label_2.setText(_translate("MainWindow", "批号"))
        self.label_3.setText(_translate("MainWindow", "生产日期"))
        self.label_5.setText(_translate("MainWindow", "不良品名称"))
        self.label_13.setText(_translate("MainWindow", "不良品描述"))
        self.label_14.setText(_translate("MainWindow", "原因分析"))
        self.label_15.setText(_translate("MainWindow", "纠正措施"))
        self.label_16.setText(_translate("MainWindow", "预防措施"))
        self.label_17.setText(_translate("MainWindow", "填写人："))
        self.pre_check.setText(_translate("MainWindow", "自审核"))
        self.btn_slparts.setText(_translate("MainWindow", "添加参与审核部门"))
        self.label_6.setText(_translate("MainWindow", "提交时间："))
        self.btn_save.setText(_translate("MainWindow", "保存修改"))
        self.label_12.setText(_translate("MainWindow", "模糊查找"))
        self.tbl_unpass.setStatusTip(_translate("MainWindow", "单击查看详细信息，右键弹出功能选项"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ongoing), _translate("MainWindow", "不良品目录"))
        self.pre_tbl_view.setStatusTip(_translate("MainWindow", "单击查看详细信息，选中后可添加评审信息！"))
        self.txt_pre_info.setPlaceholderText(_translate("MainWindow", "输入评审意见"))
        self.btn_sign_pre.setText(_translate("MainWindow", "签名"))
        self.btn_save_pre.setText(_translate("MainWindow", "保存"))
        self.label_22.setText(_translate("MainWindow", "不合格原因"))
        self.label_7.setText(_translate("MainWindow", "原因分析"))
        self.label_8.setText(_translate("MainWindow", "纠正措施"))
        self.label_9.setText(_translate("MainWindow", "预防措施"))
        self.label_10.setText(_translate("MainWindow", "技术部意见"))
        self.label_18.setText(_translate("MainWindow", "工艺部意见"))
        self.label_19.setText(_translate("MainWindow", "质量部意见"))
        self.label_20.setText(_translate("MainWindow", "技术支持部意见"))
        self.label_29.setText(_translate("MainWindow", "涉及部门"))
        self.label_21.setText(_translate("MainWindow", "采购部评审"))
        self.label_23.setText(_translate("MainWindow", "生产部评审"))
        self.label_24.setText(_translate("MainWindow", "工艺部评审"))
        self.label_25.setText(_translate("MainWindow", "物流部评审"))
        self.label_26.setText(_translate("MainWindow", "技术部评审"))
        self.label_27.setText(_translate("MainWindow", "质量部评审"))
        self.label_28.setText(_translate("MainWindow", "总经理评审"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_onpreving), _translate("MainWindow", "评审清单"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_following), _translate("MainWindow", "处理跟踪"))
        self.menu.setTitle(_translate("MainWindow", "菜单(&M)"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.act_chgpwd.setText(_translate("MainWindow", "更改密码"))
        self.act_chgpwd.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.act_chguser.setText(_translate("MainWindow", "更换用户"))
        self.act_chguser.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.act_quit.setText(_translate("MainWindow", "退出"))
        self.act_quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.act_about.setText(_translate("MainWindow", "关于"))
        self.act_about.setShortcut(_translate("MainWindow", "Ctrl+H"))


