
from threading import Thread
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
        thread = Thread(target = task, args=(name, ))
        pool.append(thread)
        thread.start()

    for thread in pool:
        thread.join()
    return 0

if __name__ == '__main__':
    main()