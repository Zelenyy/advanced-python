import fileinput

if __name__ == '__main__':

    with fileinput.input(files=['temp.txt']*10, encoding="utf-8") as f:
        for line in f:
            print(line)