import os

if __name__ == '__main__':
    os.system("conda env create -f spc_pypy.yml")
    for name in ("2.7", "3.5", "3.6", "3.7", "3.8", "3.9", "3.10"):
        os.system(f"conda create -y -n spc_py{name} python={name}")


