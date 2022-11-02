
class Test:

    def __init__(self):
        self.x = 1
        self.y = 1

    def invoke(self):
        for i in range(10):
            i += 1
            self.x = i
            print(i)
        return self.y


def main():
    test = Test()
    test.invoke()
    return 0


if __name__ == '__main__':
    main()