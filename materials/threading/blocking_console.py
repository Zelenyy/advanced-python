import time

def task(name):
    for i in range(10):
        print("Task {}, iteration {}".format(name, i), flush=True)
        time.sleep(0.25)

def main():

    while True:
        name = input()
        if name == "exit":
            break
        task(name)


    return 0

if __name__ == '__main__':
    main()