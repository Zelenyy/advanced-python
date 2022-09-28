import pathlib
import sys

from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QFileDialog, QApplication

from matplotlib.backends.backend_qt5agg import (FigureCanvas,  NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

from importlib.machinery import SourceFileLoader


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        hbox = QHBoxLayout()
        vbox.addLayout(hbox)
        button_open = QPushButton("Open")
        label = QLabel()
        button_plot = QPushButton("Plot")

        hbox.addWidget(label)
        hbox.addWidget(button_open)
        hbox.addWidget(button_plot)

        def select_name():
            name = QFileDialog.getOpenFileName(self, "Select file for plot")[0]
            if name is not None or name != "":
                self.path = name
                label.setText(name)

        button_open.clicked.connect(select_name)
        button_plot.clicked.connect(self.plot)

        self._figure = Figure(figsize=(7, 5))
        dynamic_canvas = FigureCanvas(self._figure)
        self._ax = dynamic_canvas.figure.subplots(1, 1)
        self.line = self._ax.plot([0])[0]
        self.path = None

        vbox.addWidget(dynamic_canvas)

    def plot(self):
        if self.path is not None or self.path != "":
            path = pathlib.Path(self.path)
            user = SourceFileLoader(path.stem, self.path).load_module()
            x, y = user.data()
            self.line.set_data(x,y)
            self._ax.relim()
            self._ax.autoscale()
            self._figure.tight_layout()
            self._figure.canvas.draw()


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setCentralWidget(CentralWidget())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())