from multiprocessing import Process
from mandelbrot import mandelbrot


def task(name):
    for i in range(10):
        mandelbrot()
        print("Task {}, iteration {}".format(name, i), flush=True)

def main():
    pool = []
    while True:
        name = input()
        if name == "exit":
            break
        process = Process(target = task, args = (name,))
        pool.append(process)
        process.start()

    for process in pool:
        process.join()
    return 0

if __name__ == '__main__':
    main()