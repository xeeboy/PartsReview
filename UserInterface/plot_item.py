from ui_plot_item import *

import pyqtgraph as pg
import numpy as np
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
            avg = np.average(values[-25:])  # I will use 25 samples latest, and ± 3*σ
            std = np.std(values[-25:])
            # R = max(values[-25:]) - min(values[-25:])
            ucl = avg + 3*std
            lcl = avg - 3*std
            _max = max(values)
            _min = min(values)
            # above sometimes use ± 1.88*R(bar) when large number
            pg.setConfigOptions(antialias=True)
            Plot = pg.plot(title=title)
            # Plot.plot([ucl] * len(values), pen=(255, 0, 0), name='Red curve')
            Plot.plot(values, pen=(0, 255, 0), name="Green curve")
            Plot.plot([avg] * len(values), pen=(255, 255, 255), name='Yellow curve')
            # Plot.plot([lcl] * len(values), pen=(0, 0, 255), name='Blue curve')
            Plot.plot([_max] * len(values), pen=(100, 0, 255), name='max curve')
            Plot.plot([_min] * len(values), pen=(0, 100, 255), name='min curve')
        except Exception as e:
            print(e)

