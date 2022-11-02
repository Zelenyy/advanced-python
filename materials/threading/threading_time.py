import time
from threading import Thread

from mandelbrot import mandelbrot


def task(name):
    for i in range(5):
        mandelbrot()
        print("Task {}, iteration {}".format(name, i), flush=True)

def main():
    tic = time.perf_counter()
    pool = []
    for i in range(5):
        thread = Thread(target = task, args=("Task {}".format(i),))
        pool.append(thread)
        thread.start()

    for thread in pool:
        thread.join()
    toc = time.perf_counter()
    print(toc - tic, "s")
    return 0

if __name__ == '__main__':
    main()