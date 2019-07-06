from ui_plot_item import *

import pyqtgraph as pg
from datetime import datetime
from PyQt5.QtWidgets import QRadioButton


class PlotItem(QtWidgets.QDialog, Ui_plot_item):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.btn_isok.accepted.connect(self.show_chart)

    def show_chart(self):
        try:
            col_n = 0
            title = ''
            for ctl in self.findChildren(QRadioButton):
                if ctl.isChecked():
                    col_n = self.parent.test_result_fields.index(ctl.text())
                    title = '当前筛选范围的{}折线图'.format(ctl.text())
                    break
            model = self.parent.test_result_model
            values = []
            for i in range(model.rowCount()):
                v = model.item(i, col_n).text()
                if v:
                    values.append(abs(float(v)))
                    print(model.item(i, 3).text())
            pg.setConfigOptions(antialias=True)
            # TODO Show SPC chart
            pg.plot(values, pen=(255, 0, 0), name="Red curve", title=title)
        except Exception as e:
            print(e)

