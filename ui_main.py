# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1129, 790)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/backup/icons/parameterreview_32px_26157_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_ongoing = QtWidgets.QWidget()
        self.tab_ongoing.setObjectName("tab_ongoing")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_ongoing)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem)
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
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 6, 1, 1)
        self.unpassname = QtWidgets.QLineEdit(self.tab_ongoing)
        self.unpassname.setReadOnly(True)
        self.unpassname.setObjectName("unpassname")
        self.gridLayout.addWidget(self.unpassname, 1, 5, 1, 1)
        self.batch = QtWidgets.QLineEdit(self.tab_ongoing)
        self.batch.setReadOnly(True)
        self.batch.setObjectName("batch")
        self.gridLayout.addWidget(self.batch, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_ongoing)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.prodate = QtWidgets.QLineEdit(self.tab_ongoing)
        self.prodate.setReadOnly(True)
        self.prodate.setObjectName("prodate")
        self.gridLayout.addWidget(self.prodate, 0, 9, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_ongoing)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.unpasstype = QtWidgets.QLineEdit(self.tab_ongoing)
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
        self.unpassqty.setReadOnly(True)
        self.unpassqty.setObjectName("unpassqty")
        self.gridLayout.addWidget(self.unpassqty, 1, 9, 1, 1)
        self.ID = QtWidgets.QLineEdit(self.tab_ongoing)
        self.ID.setReadOnly(True)
        self.ID.setObjectName("ID")
        self.gridLayout.addWidget(self.ID, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 10, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.tab_ongoing)
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
        self.describe.setReadOnly(True)
        self.describe.setObjectName("describe")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.describe)
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.result = QtWidgets.QTextEdit(self.frame)
        self.result.setEnabled(True)
        self.result.setObjectName("result")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.result)
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.correctiveaciton = QtWidgets.QTextEdit(self.frame)
        self.correctiveaciton.setObjectName("correctiveaciton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.correctiveaciton)
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.precaution = QtWidgets.QTextEdit(self.frame)
        self.precaution.setObjectName("precaution")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.precaution)
        self.label_17 = QtWidgets.QLabel(self.frame)
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
        self.parts.setObjectName("parts")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.parts)
        self.btn_slparts = QtWidgets.QPushButton(self.frame)
        self.btn_slparts.setObjectName("btn_slparts")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.btn_slparts)
        self.pre_time = QtWidgets.QLabel(self.frame)
        self.pre_time.setText("")
        self.pre_time.setObjectName("pre_time")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.pre_time)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_6)
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
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_2.addWidget(self.lineEdit_11)
        self.btn_search = QtWidgets.QPushButton(self.frame_3)
        self.btn_search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/backup/icons/search.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_2.addWidget(self.btn_search)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.btn_caseto = QtWidgets.QPushButton(self.frame_3)
        self.btn_caseto.setObjectName("btn_caseto")
        self.horizontalLayout_2.addWidget(self.btn_caseto)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.tbl_unpass = QtWidgets.QTableView(self.frame_2)
        self.tbl_unpass.setObjectName("tbl_unpass")
        self.verticalLayout_5.addWidget(self.tbl_unpass)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/backup/icons/dir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_ongoing, icon2, "")
        self.tab_dealidea = QtWidgets.QWidget()
        self.tab_dealidea.setObjectName("tab_dealidea")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_dealidea)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/backup/icons/dealidea.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_dealidea, icon3, "")
        self.tab_onpreving = QtWidgets.QWidget()
        self.tab_onpreving.setObjectName("tab_onpreving")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/backup/icons/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_onpreving, icon4, "")
        self.tab_following = QtWidgets.QWidget()
        self.tab_following.setObjectName("tab_following")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/backup/icons/gps_navigation_position_positioning_tracking_32px_1225459_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_following, icon5, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.act_changepwd = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/backup/icons/password32px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_changepwd.setIcon(icon6)
        self.act_changepwd.setObjectName("act_changepwd")
        self.act_chguser = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/backup/icons/user32px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_chguser.setIcon(icon7)
        self.act_chguser.setObjectName("act_chguser")
        self.action_quit = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("C:/Users/Administrator/.designer/backup/icons/quit128px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_quit.setIcon(icon8)
        self.action_quit.setObjectName("action_quit")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setIcon(icon2)
        self.action_about.setObjectName("action_about")
        self.menu.addAction(self.act_changepwd)
        self.menu.addAction(self.act_chguser)
        self.menu.addSeparator()
        self.menu.addAction(self.action_quit)
        self.menuHelp.addAction(self.action_about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.action_quit.triggered.connect(MainWindow.close)
        self.lineEdit_11.returnPressed.connect(self.btn_search.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.result, self.correctiveaciton)
        MainWindow.setTabOrder(self.correctiveaciton, self.precaution)
        MainWindow.setTabOrder(self.precaution, self.lineEdit_11)
        MainWindow.setTabOrder(self.lineEdit_11, self.btn_search)
        MainWindow.setTabOrder(self.btn_search, self.btn_caseto)
        MainWindow.setTabOrder(self.btn_caseto, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.pre_check)
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
        self.label_17.setText(_translate("MainWindow", "自审人："))
        self.pre_check.setText(_translate("MainWindow", "自审核"))
        self.btn_slparts.setText(_translate("MainWindow", "添加参与审核部门"))
        self.label_6.setText(_translate("MainWindow", "自审时间："))
        self.label_12.setText(_translate("MainWindow", "模糊查找"))
        self.btn_caseto.setText(_translate("MainWindow", "Case To"))
        self.tbl_unpass.setStatusTip(_translate("MainWindow", "单击查看详细信息，双击case相关人员"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ongoing), _translate("MainWindow", "不良品目录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dealidea), _translate("MainWindow", "处理意见"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_onpreving), _translate("MainWindow", "待评审"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_following), _translate("MainWindow", "处理跟踪"))
        self.menu.setTitle(_translate("MainWindow", "菜单(&M)"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.act_changepwd.setText(_translate("MainWindow", "更改密码"))
        self.act_changepwd.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.act_chguser.setText(_translate("MainWindow", "更换用户"))
        self.act_chguser.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.action_quit.setText(_translate("MainWindow", "退出"))
        self.action_quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_about.setText(_translate("MainWindow", "关于"))
        self.action_about.setShortcut(_translate("MainWindow", "Ctrl+H"))

