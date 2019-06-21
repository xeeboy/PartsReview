from pyodbc import connect
from configparser import ConfigParser
from PyQt5.QtGui import QStandardItem, QStandardItemModel

config = ConfigParser()
config.read('config.ini')
DB_FILE = config.get('DBPath', 'path')


class AccDb:
    def __init__(self):
        self._conn = connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + DB_FILE)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cursor.close()
        self._conn.close()

    def get_rst(self, sql):
        recordset = self._cursor.execute(sql).fetchall()
        return recordset

    def modify_db(self, sql):
        self._cursor.execute(sql)
        self._cursor.commit()


def get_model(fields, sql):
    """set and return a QstandItemModel"""
    db = AccDb()
    model = QStandardItemModel()
    with db:
        rst = db.get_rst(sql)
    n = len(rst)
    for i in range(len(fields)):
        item = QStandardItem(fields[i])
        model.setHorizontalHeaderItem(i, item)
    for rown in range(n):
        for coln in range(len(fields)):
            content = rst[rown][coln]
            if coln == 0:
                content = '%06d' % content
            item = QStandardItem(content)
            model.setItem(rown, coln, item)
    return model

