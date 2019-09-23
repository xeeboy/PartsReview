"""Connect database and generate model for tbl_view"""

from pymysql import cursors, connect
from configparser import ConfigParser
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt

#  for using when pymysql connect Access
config = ConfigParser()
config.read(r'Configration\config.ini')
HOST = config.get('DBInfo', 'host')
PORT = config.getint('DBInfo', 'port')  # port must be type int
DB_NAME = config.get('DBInfo', 'db_name')

CORPID = config.get('TokenInfo', 'corpid')
SECRET = config.get('TokenInfo', 'secret')
AGENTID = config.get('TokenInfo', 'agentid')


class MysqlDb:
    """Connect to Mysql server"""
    def __init__(self, user='root', password='123456',
                 cursor_type=cursors.DictCursor):
        self._cnn = connect(host=HOST, port=PORT, user=user, password=password,
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


def is_number(obj):
    try:
        float(obj)
        return True
    except ValueError:
        return False


def get_model(fields, sql):
    """set and return a QStandItemModel"""
    db = MysqlDb()
    model = QStandardItemModel()
    with db:
        rst = db.get_rst(sql)
    n = len(rst)
    model.setHorizontalHeaderLabels(fields)
    for rown in range(n):
        for coln in range(len(fields)):
            content = list(rst[rown].values())[coln]
            content = '' if content is None else content
            item = QStandardItem()
            v = str(content)
            if is_number(v):
                item.setData(content, Qt.EditRole)
            else:
                item.setText(v)
            model.setItem(rown, coln, item)
    return model

