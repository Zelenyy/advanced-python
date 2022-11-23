import sys

from PySide2.QtCore import QObject, Slot, Signal
from PySide2.QtWidgets import QMainWindow, QAction, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton



class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super(MainWindow, self).__init__()
        geometry = app.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.4, geometry.height() * 0.7)


class Controller(QObject):
    send = Signal((int,), (str,))


class CentralWidget(QWidget):
    def __init__(self, controller: Controller):
        super(CentralWidget, self).__init__()
        self.controller = controller
        self.init_UI()

    def init_UI(self):
        vbox_layout = QVBoxLayout()
        button_1 = QPushButton("Button 1")
        button_2 = QPushButton("Button 2")
        button_3 = QPushButton("Button 3")
        button_4 = QPushButton("Button 4")
        button_5 = QPushButton("Button 5")
        vbox_layout.addWidget(button_1)
        vbox_layout.addWidget(button_2)
        vbox_layout.addWidget(button_3)
        vbox_layout.addWidget(button_4)
        vbox_layout.addWidget(button_5)
        vbox_layout.addStretch()
        self.setLayout(vbox_layout)

        button_1.clicked.connect(lambda : self.controller.send.emit(10))
        button_2.clicked.connect(lambda : self.controller.send.emit("hello"))
        button_3.clicked.connect(lambda : self.controller.send[str].emit("hello str"))
        button_4.clicked.connect(lambda : self.controller.send[str].emit(10))
        button_5.clicked.connect(lambda : self.controller.send[int].emit(10))


def consumer_0():
    print("cons 0")

def consumer_1(arg):
    print("cons 1",type(arg), arg)

@Slot(int)
def consumer_2(arg):
    print("cons 2",type(arg), arg)

@Slot(str)
def consumer_3(arg):
    print("cons 3",type(arg), arg)

@Slot(int)
@Slot(str)
def consumer_4(arg):
    print("cons 4",type(arg), arg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow(app)
    controller = Controller()

    controller.send.connect(consumer_0)
    controller.send.connect(consumer_1)
    controller.send.connect(consumer_2)
    controller.send.connect(consumer_3)
    controller.send.connect(consumer_4)

    controller.send[int].connect(consumer_0)
    controller.send[int].connect(consumer_1)
    controller.send[int].connect(consumer_2)
    controller.send[int].connect(consumer_3)
    controller.send[int].connect(consumer_4)

    controller.send[str].connect(consumer_0)
    controller.send[str].connect(consumer_1)
    controller.send[str].connect(consumer_2)
    controller.send[str].connect(consumer_3)
    controller.send[str].connect(consumer_4)

    widget = CentralWidget(controller)
    main.setCentralWidget(widget)
    main.show()
    app.exec_()