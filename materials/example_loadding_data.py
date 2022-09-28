import numpy as np


def data():
    x = np.linspace(0, 10, 300)
    return x, np.sin(x)