import numpy as np


async def mandelbrot():
    pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
    ppoints, qpoints = 200, 200
    max_iterations = 300
    infinity_border = 100
    image = np.zeros((ppoints, qpoints))
    for ip, p in enumerate(np.linspace(pmin, pmax, ppoints)):
        for iq, q in enumerate(np.linspace(qmin, qmax, qpoints)):
            c = p + 1j * q
            z = 0
            for k in range(max_iterations):
                z = z ** 2 + c
                if abs(z) > infinity_border:
                    image[ip, iq] = 1
                    break