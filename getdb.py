"""Connect database and generate model for tbl_view"""

import pymysql
from configparser import ConfigParser
from PyQt5.QtGui import QStandardItem, QStandardItemModel

#  for using when pymysql connect Access
config = ConfigParser()
config.read('config.ini')
HOST = config.get('DBInfo', 'host')
PORT = config.getint('DBInfo', 'port')
DB_NAME = config.get('DBInfo', 'db_name')


class MysqlDb:
    """conncet to Mysql server"""
    def __init__(self, user='root', password='123456',
                 cursor_type=pymysql.cursors.DictCursor):
        self._cnn = pymysql.connect(host=HOST, port=PORT, user=user, password=password,
                                    charset='utf8', cursorclass=cursor_type)
        self._cursor = self._cnn.cursor()
        self._con_db(DB_NAME)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cnn.close()
        self._cursor.close()

    def _con_db(self, db_name):
        self.modify_db('use %s' % db_name)

    def modify_db(self, sql):
        self._cursor.execute(sql)
        self._cnn.commit()

    def get_rst(self, sql):
        self._cursor.execute(sql)
        return self._cursor.fetchall()


def get_model(fields, sql):
    """set and return a QstandItemModel"""
    db = MysqlDb()
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
            content = '' if content is None else content
            item = QStandardItem(str(content))
            model.setItem(rown, coln, item)
    return model

