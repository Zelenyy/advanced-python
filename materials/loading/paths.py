from pathlib import Path

print(__name__)


FILE_PATH = Path(__file__)
PACKAGE_PATH = FILE_PATH.absolute().parent

print(FILE_PATH)
print(PACKAGE_PATH)

if __name__ == '__main__':
    pass
