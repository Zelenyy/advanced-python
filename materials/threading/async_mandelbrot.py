import numpy as np

time_scale = 1.5

async def mandelbrot():
    pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
    ppoints, qpoints = int(200 / time_scale), int(200/ time_scale)
    max_iterations = int(300 / time_scale)
    infinity_border = int(100 / time_scale)
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
    return image