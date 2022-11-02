import asyncio
import os
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
from threading import Thread

from PySide2.QtWidgets import QMainWindow, QApplication, QTabWidget, QWidget, QVBoxLayout, QPushButton, QProgressBar, \
    QHBoxLayout, QLabel
from mandelbrot import mandelbrot
btn_style = """
QPushButton {
  color: blue;
  background-color: white;
  border: 2px solid blue;
  border-radius: 4px;
  height: 36px;
  text-transform: uppercase;
  font-weight: bold;
}

QPushButton:checked,
QPushButton:pressed {
  color: red;
  background-color: white;
}

QPushButton:hover {
  background-color: green;
}
"""
lbl_style = """
QLabel{
  color: blue;
  text-transform: uppercase;
  font-weight: bold;
  
}
"""


class BaseWidget(QWidget):

    def __init__(self, n):
        self.n = n
        super(BaseWidget, self).__init__()
        vbox = QVBoxLayout(self)
        self.tlbl = QLabel("Execution time: ")
        self.tlbl.setStyleSheet(lbl_style)
        vbox.addWidget(self.tlbl)
        hbox = QHBoxLayout()
        btn = QPushButton("Start")
        btn.setStyleSheet(btn_style)
        lbl = QLabel()
        hbox.addWidget(btn)
        hbox.addWidget(lbl)

        def update():
            lbl.setText(str(random.randint(0, 100)))

        btn.clicked.connect(update)
        vbox.addLayout(hbox)

        btn = QPushButton("Start")
        btn.setStyleSheet(btn_style)
        vbox.addWidget(btn)
        btn.clicked.connect(self.start)

        self.pb_list = []
        for i in range(n):
            pb = QProgressBar()
            pb.setRange(0, 100)
            pb.setValue(0)
            vbox.addWidget(pb)
            self.pb_list.append(pb)

        vbox.addStretch()

    def start(self):
        pass


class BlockingWidget(BaseWidget):

    def start(self):
        for pb in self.pb_list:
            pb.setValue(0)

        for pb in self.pb_list:
            for i in range(1, 11):
                time.sleep(0.2)
                pb.setValue(10*i)


class ThreadingWidget(BaseWidget):

    def start(self):
        tic = time.perf_counter()
        for pb in self.pb_list:
            pb.setValue(0)

        def task(indx):
            pb = self.pb_list[indx]
            for i in range(1, 11):
                mandelbrot()
                pb.setValue(10 * i)

        with ThreadPoolExecutor(max_workers=5) as executor:
            pool = []
            for i in range(self.n):
                pool.append(executor.submit(task, i))
            for future in pool:
                future.result()
        toc = time.perf_counter()
        self.tlbl.setText(f"Execution time: {toc-tic:.1f}")


class NonBlockingMainWidget(BaseWidget):

    def start(self):
        def _start():
            for pb in self.pb_list:
                pb.setValue(0)

            for pb in self.pb_list:
                for i in range(1, 11):
                    time.sleep(0.2)
                    pb.setValue(10*i)
        thread = Thread(target=_start)
        thread.start()


class AsyncWithoutLatencyWidget(BaseWidget):

    def start(self):

        async def task(i):
            pb = self.pb_list[i]
            for i in range(1, 11):
                mandelbrot()
                pb.setValue(10 * i)

        async def main():
            await asyncio.gather(*(task(i) for i in range(self.n)))

        asyncio.run(main())


class AsyncWithLatencyWidget(BaseWidget):

    def start(self):

        async def task(i):
            pb = self.pb_list[i]
            for i in range(1, 11):
                await asyncio.sleep(random.randint(0,10)/10)
                mandelbrot()
                pb.setValue(10 * i)

        async def main():
            await asyncio.gather(*(task(i) for i in range(self.n)))

        asyncio.run(main())


def mp_task(i):
    mandelbrot()
    return i


class MultyProcessingWidget(BaseWidget):

    def start(self):
        tic = time.perf_counter()
        with Pool(processes=os.cpu_count()) as p:
            for i in range(1,11):
                for indx, value in enumerate(p.map(mp_task, self.n*[i])):
                    self.pb_list[indx].setValue(10*value)

        toc = time.perf_counter()
        self.tlbl.setText(f"Execution time: {toc-tic:.1f}")


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super(MainWindow, self).__init__()
        geometry = app.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.5, geometry.height() * 0.7)
        tab_widget = QTabWidget()
        self.setCentralWidget(tab_widget)
        tab_widget.addTab(MultyProcessingWidget(os.cpu_count()), "MULTYPROCESSING")
        tab_widget.addTab(AsyncWithLatencyWidget(10), "ASYNC_WITH")
        tab_widget.addTab(AsyncWithoutLatencyWidget(5), "ASYNC_WITHOUT")
        tab_widget.addTab(NonBlockingMainWidget(5), "NON_BLOCKING_MAIN")
        tab_widget.addTab(ThreadingWidget(10), "THREADING")
        tab_widget.addTab(BlockingWidget(3), "BLOCKING")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow(app)
    main.show()
    app.exec_()