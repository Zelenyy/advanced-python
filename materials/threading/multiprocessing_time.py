import time
from multiprocessing import Process
from mandelbrot import mandelbrot


def task(name):
    for i in range(5):
        mandelbrot()
        print("Task {}, iteration {}".format(name, i), flush=True)

def main():
    tic = time.perf_counter()
    pool = []
    for i in range(16):
        process = Process(target = task, args = ("task_{}".format(i),))
        pool.append(process)
        process.start()

    for process in pool:
        process.join()
    toc = time.perf_counter()
    print(toc - tic, "s")
    return 0

if __name__ == '__main__':
    main()