def clear_unpass_info(self):
    for ctl in [self.ID, self.batch, self.unpasstype, self.unpassname, self.unpassqty,
                self.describe, self.customer]:
        ctl.setText(None)
    self.prodate.setDate(QDate.currentDate())


def save_new_unpass(self):
    batch, prodate, unpasstype, unpassname, unpassqty, describe, customer = self.batch.text(), self.prodate.text(), self.unpasstype.text(), self.unpassname.text(), self.unpassqty.text(), self.describe.toPlainText(), self.customer.text()
    if all([batch, prodate, unpasstype, unpassname, unpassqty, describe, customer]):
        sql = "INSERT INTO 不合格品登记 (批号,生产日期,不良品种类,不良品名称,数量Kg,不合格描述,客户) " \
              "VALUES ('{}','{}','{}','{}','{}','{}','{}')" \
              "".format(batch, prodate, unpasstype, unpassname, float(unpassqty),
                        describe, customer)
        _db = MysqlDb()
        with _db:
            try:
                _db.modify_db(sql)
                self.set_tbl_unpass(TBL_UNPASS_SQL)
            except Exception as e:
                user_info.log2txt('登记新不合格品时发生错误：{}'.format(e))