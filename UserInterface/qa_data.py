import user_info

from ui_qa_data import *
from new_unpass import NewUnpass
from getdb import MysqlDb, get_model, QStandardItem

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QMessageBox, QTableView, QMenu, QAction

TEST_ITEMS = (
    '批号', '表面判定', 'RoSH', '性能判定', '密度', '拉伸强度', '断裂伸长率', '低冲温度',
    '断裂根数', '体积电阻率温度','体积电阻率', '硬度标准', '硬度', '200℃热稳定时间',
    '介电强度', '氧指数', '熔融指数', '快速水分测定', '热变形温度', '热变形', '检验员')


class AddDataForm(QtWidgets.QMainWindow, Ui_QAData):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.date_produce.setDate(QDate.currentDate())
        self.date_test.setDate(QDate.currentDate())
        self.btn_test_clear.clicked.connect(self.clear_pro_info)
        self.btn_test_tounpass.clicked.connect(self.to_unpass)
        self.btn_search_need_modi.clicked.connect(self.test_search)
        self.test_data_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.test_data_view.customContextMenuRequested.connect(self.rclick_test_data_view)

        self.test_data_view.setSelectionMode(QTableView.SingleSelection)
        self.test_data_view.setStyleSheet(
            "selection-color: rgb(255, 0, 127);\nselection-background-color: rgb(85, 255, 127);")

        db = MysqlDb()
        with db:
            self.rst = db.get_rst("SELECT DISTINCT 客户,产品型号,颜色 FROM 产品信息")
        self.comb_test_coustomer.addItems(set(r['客户'] for r in self.rst))
        self.comb_test_coustomer.setCurrentIndex(-1)
        self.comb_test_coustomer.currentTextChanged.connect(self.set_pro_type_items)
        self.comb_pro_type.currentTextChanged.connect(self.set_pro_color_items)
        self.btn_test_save.clicked.connect(self.save_pro_info)

    def rclick_test_data_view(self):
        popMenu = QMenu()
        action_del = QAction('删除', self)
        action_del.setIcon(QIcon('icons/delete_file_32px.ico'))
        action_flush = QAction('刷新', self)
        action_flush.setIcon(QIcon('icons/dir.png'))
        popMenu.addAction(action_flush)
        popMenu.addAction(action_del)
        popMenu.triggered.connect(self.processtrigger_rclick)
        popMenu.exec_(QCursor.pos())

    def processtrigger_rclick(self, act):
        row = self.test_data_view.currentIndex().row()
        if row != -1:
            try:
                db = MysqlDb()
                with db:
                    batch = self.model.item(row, 0).text()
                    if act.text() == '刷新':
                        trans = []
                        for i in range(1, self.model.columnCount()):
                            field = self.model.horizontalHeaderItem(i).text()
                            v = self.model.item(row, i).text()
                            if field == '表面判定' or field == 'RoSH':
                                v = 1 if v.upper() == 'PASS' else 0
                            if v:
                                field_v = "{}='{}'".format(field, v)
                                trans.append(field_v)
                        sql = "UPDATE 常规性能 SET {} WHERE 批号='{}'".format(','.join(trans), batch)
                        db.modify_db(sql)
                        QMessageBox.information(self, '提示', '操作已完成！')
                    elif act.text() == '删除':
                        reply = QMessageBox.question(self, 'Message', '确认删除<{}>?'.format(batch),
                                                     QMessageBox.Yes | QMessageBox.No,
                                                     QMessageBox.No)
                        if reply == QMessageBox.Yes:
                            sql_1 = "DELETE FROM 常规性能 WHERE 批号='{}'".format(batch)
                            sql_2 = "DELETE FROM 产品信息 WHERE 批号='{}'".format(batch)
                            try:
                                db._cursor.execute(sql_1)
                                db._cursor.execute(sql_2)
                                db._cnn.commit()
                                QMessageBox.information(self, '提示', '操作已完成！')
                            except Exception as e1:
                                db._cnn.rollback()
                                QMessageBox.warning(self, '错误', '删除失败')
                                user_info.log2txt('删除检测数据时发生错误：{}'.format(e1))
                    self.test_search()
            except Exception as e2:
                QMessageBox.warning(self, '错误', '操作失败')
                user_info.log2txt('更新检测数据时发生错误：{}'.format(e2))

    def set_pro_type_items(self, coustomer):
        self.comb_pro_type.clear()  # remove all current items
        self.comb_pro_type.addItems(
            set((r['产品型号'] for r in self.rst if r['客户'] == coustomer)))

    def set_pro_color_items(self, pro_name):
        self.comb_pro_color.clear()
        self.comb_pro_color.addItems(
            set((r['颜色'] for r in self.rst if r['产品型号'] == pro_name)))

    def clear_pro_info(self):
        self.test_batch.setText(None)
        self.comb_test_coustomer.setCurrentIndex(-1)
        self.comb_pro_type.setCurrentIndex(-1)
        self.comb_pro_color.setCurrentIndex(-1)
        self.date_produce.setDate(QDate.currentDate())
        self.date_test.setDate(QDate.currentDate())

    def to_unpass(self):
        new_unpass_frm = NewUnpass(self)
        new_unpass_frm.new_batch.setText(self.test_batch.text())
        new_unpass_frm.comb_new_coustom.setCurrentText(self.comb_test_coustomer.currentText())
        new_unpass_frm.comb_new_unpassname.setCurrentText(self.comb_pro_type.currentText())
        new_unpass_frm.date_produce.setDate(self.date_produce.date())
        new_unpass_frm.show()

    def test_search(self):
        kw = self.keyword.text()
        sql = "SELECT a.批号,IF(表面判定=TRUE,'PASS',IF(表面判定 IS NULL,NULL,'UNPASS'))," \
              "IF(RoSH=TRUE,'PASS',IF(RoSH IS NULL,NULL,'UNPASS')),{} " \
              "FROM 产品信息 a INNER JOIN 常规性能 b ON a.批号=b.批号 " \
              "WHERE a.批号 like '%{}%'" .format(','.join(TEST_ITEMS[3:]), kw)
        self.set_test_data_view(sql)

    def save_pro_info(self):
        batch, coustomer, pro_name, pro_color, pro_date, test_date = \
            self.test_batch.text(), self.comb_test_coustomer.currentText(), \
            self.comb_pro_type.currentText(), self.comb_pro_color.currentText(), \
            self.date_produce.text(), self.date_test.text()
        if all([batch, coustomer, pro_name, pro_color, pro_date, test_date]):
            db = MysqlDb()
            with db:
                try:
                    sql_info = "INSERT INTO 产品信息 (批号, 客户, 产品型号, 颜色, 生产日期, 检验日期)" \
                               " VALUES ('{}', '{}', '{}', '{}', '{}', '{}')" \
                               "".format(batch, coustomer, pro_name, pro_color, pro_date,
                                         test_date)
                    sql_performance = "INSERT INTO 常规性能 SET 批号='{}'".format(batch)
                    db._cursor.execute(sql_info)
                    db._cursor.execute(sql_performance)
                    db._cnn.commit()
                    sql_for_new = "SELECT {} FROM 常规性能 WHERE 批号='{}'" \
                                  "".format(','.join(TEST_ITEMS), batch)
                    #  show 20 items of the same product's test result recently
                    sql_other_same = "SELECT a.批号,IF(表面判定=TRUE,'PASS',IF(表面判定 IS NULL,NULL,'UNPASS'))," \
                                     "IF(RoSH=TRUE,'PASS',IF(RoSH IS NULL,NULL,'UNPASS')),{} FROM 产品信息 a INNER JOIN 常规性能 b " \
                                     "ON a.批号=b.批号 WHERE CONCAT(客户,产品型号) like '%{}%' AND a.批号<>'{}' LIMIT 20" \
                                     "".format(','.join(TEST_ITEMS[3:]), coustomer + pro_name, batch)
                    self.set_test_data_view('{} UNION {}'.format(sql_for_new, sql_other_same))
                except Exception as e:
                    db._cnn.rollback()
                    QMessageBox.critical(self, '逻辑错误', '可能已存在相同的批号！')
                    user_info.log2txt('登记新产品信息时错误：{}'.format(e))
        else:
            QMessageBox.warning(self, '警告', '缺少必要产品信息！')

    def set_test_data_view(self, sql):
        self.model = get_model(TEST_ITEMS, sql)
        self.test_data_view.setSelectionBehavior(QTableView.SelectRows)
        for i in range(self.model.rowCount()):
            v = self.model.item(i, 10).text()
            if v:
                self.model.setItem(i, 10, QStandardItem('%.2e'%int(v)))
        self.test_data_view.setModel(self.model)
        self.test_data_view.resizeColumnsToContents()
