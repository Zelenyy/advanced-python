import os
import sys

if __name__ == '__main__':
    if sys.argv[1] in ("py37", "py310", "pypy"):
        name = sys.argv[1]
    else:
        sys.exit()
    os.system(f"conda activate spc-{name}")
    os.system("python --version")
    os.system("conda deactivate")
