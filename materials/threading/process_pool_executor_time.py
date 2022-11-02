import time
from concurrent.futures import ProcessPoolExecutor
from mandelbrot import mandelbrot


def task(name):
    for i in range(10):
        mandelbrot()
        print("Task {}, iteration {}".format(name, i), flush=True)

def main():
    tic = time.perf_counter()
    with ProcessPoolExecutor(max_workers=8) as executor:
        pool = []
        for i in range(5):
            pool.append(executor.submit(task, "task_10 {}".format(i)))
        for future in pool:
            future.result()
    toc = time.perf_counter()
    print(toc - tic, "s")
    return 0

if __name__ == '__main__':
    main()