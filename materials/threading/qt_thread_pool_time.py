import time
from threading import Thread

from mandelbrot import mandelbrot
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool, QCoreApplication


class Task(QRunnable):

    def __init__(self, name):
        super(Task, self).__init__()
        self.name = name

    def run(self):
        for i in range(4):
            mandelbrot()
            print("Task {}, iteration {}".format(self.name, i), flush=True)


def start_task():
    tic = time.perf_counter()
    threadpool = QThreadPool.globalInstance()
    tasks = []
    for i in range(8):
        tasks.append(Task("Task {}".format(i)))

    for task in tasks:
        threadpool.start(task)

    threadpool.waitForDone()
    toc = time.perf_counter()
    print(toc - tic, "s")
    # QCoreApplication.instance().quit()

def main():
    # app = QCoreApplication()
    start_task()
    # app.exec_()
    return 0

if __name__ == '__main__':
    main()