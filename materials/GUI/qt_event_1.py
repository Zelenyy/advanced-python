import sys

from PySide2.QtCore import QObject, Slot
from PySide2.QtWidgets import QMainWindow, QAction, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton



class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super(MainWindow, self).__init__()
        geometry = app.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.4, geometry.height() * 0.7)

def hello():
    print("Hello 2")

@Slot()
def hello_slot():
    print("Hello 3")

class CentralWidget(QWidget):
    def __init__(self):
        super(CentralWidget, self).__init__()
        self.init_UI()

    def init_UI(self):
        vbox_layout = QVBoxLayout()
        button_1 = QPushButton("Button 1")
        button_2 = QPushButton("Button 2")
        button_3 = QPushButton("Button 3")
        vbox_layout.addWidget(button_1)
        vbox_layout.addWidget(button_2)
        vbox_layout.addWidget(button_3)
        vbox_layout.addStretch()
        self.setLayout(vbox_layout)

        button_1.clicked.connect(lambda : print("Hello 1"))
        button_2.clicked.connect(hello)
        button_3.clicked.connect(hello_slot)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow(app)
    widget = CentralWidget()
    main.setCentralWidget(widget)
    main.show()
    app.exec_()