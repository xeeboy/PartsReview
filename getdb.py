from pyodbc import connect
from configparser import ConfigParser

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
