import sys

from PySide2.QtWidgets import QMainWindow, QAction, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super(MainWindow, self).__init__()
        self.setWindowTitle("This is Window title")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        self.file_menu.addAction(exit_action)
        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("This is status bar")

        # Window dimensions
        geometry = app.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.4, geometry.height() * 0.7)


class CentralWidget(QWidget):
    def __init__(self):
        super(CentralWidget, self).__init__()
        self.init_UI()

    def init_UI(self):
        hbox_layout = QHBoxLayout()

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(QPushButton("Button 1"))
        vbox_layout.addWidget(QPushButton("Button 2"))
        vbox_layout.addWidget(QPushButton("Button 3"))
        vbox_layout.addStretch()
        hbox_layout.addLayout(vbox_layout)

        vbox_layout = QVBoxLayout()
        for i in range(3):
            vbox_layout.addWidget(QPushButton("Button {}".format(i)))
        hbox_layout.addLayout(vbox_layout)

        vbox_layout = QVBoxLayout()
        for i in range(3):
            vbox_layout.addWidget(QPushButton("Button {}".format(i)))
        hbox_layout.addLayout(vbox_layout)
        self.setLayout(hbox_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow(app)

    widget = CentralWidget()
    main.setCentralWidget(widget)
    main.show()
    app.exec_()