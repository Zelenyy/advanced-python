import time

from mandelbrot import mandelbrot


def task(name):
    for i in range(2):
        mandelbrot()
        print("Task {}, iteration {}".format(name, i), flush=True)

def main():
    tic = time.perf_counter()
    for i in range(2):
        task("task_10 {}".format(i))
    toc = time.perf_counter()
    print(toc - tic, "s")
    return 0

if __name__ == '__main__':
    main()