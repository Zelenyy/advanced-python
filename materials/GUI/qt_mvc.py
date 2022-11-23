import sys

import numpy as np
from PySide2 import QtCore
from PySide2.QtCore import QObject, Slot, QAbstractItemModel, QModelIndex
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QMainWindow, QAction, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, \
    QTreeView, QListView, QTableView


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super(MainWindow, self).__init__()
        geometry = app.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.6, geometry.height() * 0.9)


class CentralWidget(QWidget):
    def __init__(self, model):
        super(CentralWidget, self).__init__()
        self.model = model
        self.init_UI()

    def init_UI(self):
        vbox_layout = QVBoxLayout()

        list = QListView()
        list.setModel(self.model)

        table = QTableView()
        table.setModel(self.model)

        tree = QTreeView()
        tree.setModel(self.model)

        vbox_layout.addWidget(list)
        vbox_layout.addWidget(table)
        vbox_layout.addWidget(tree)
        # vbox_layout.addStretch()
        self.setLayout(vbox_layout)

def add_data(item: QStandardItem, array: np.ndarray):
    dt = array.dtype
    for icol, name in enumerate(dt.names):
        sub_dtype = dt[name]
        for irow, value in enumerate(array[name]):
            new_item = QStandardItem(str(value))
            item.setChild(irow, icol, new_item)
            if sub_dtype.names is not None:
                for subname in sub_dtype.names:
                    inner_item = QStandardItem(subname + ":" +str(value[subname]))
                    new_item.appendRow(inner_item)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow(app)

    dt =  np.dtype([
    ("angle", [
        ("theta", "d"),
        ("phi", "d"),
    ]),
    ("id", "i"),
    ("parent_id", "i"),
    ("energy", "d"),
    ("radius", "d", (10,10)),
])
    array = np.ones(10, dtype=dt)

    model = QStandardItemModel()
    parentItem = model.invisibleRootItem()
    add_data(parentItem, array)
    widget = CentralWidget(model)
    main.setCentralWidget(widget)
    main.show()
    app.exec_()
