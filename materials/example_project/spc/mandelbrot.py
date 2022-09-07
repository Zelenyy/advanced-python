"""
The Mandelbrot set has its origin in complex dynamics, a field first investigated by the French mathematicians Pierre Fatou and Gaston Julia at the beginning of the 20th century. This fractal was first defined and drawn in 1978 by Robert W. Brooks and Peter Matelski as part of a study of Kleinian groups.[3] On 1 March 1980, at IBM's Thomas J. Watson Research Center in Yorktown Heights, New York, Benoit Mandelbrot first saw a visualization of the set.
"""

import numpy as np


def mandelbrot(n_points = 200, max_iterations = 300):
    """
    There are many programs and algorithms used to plot the Mandelbrot set and other fractals, some of which are described in fractal-generating software. These programs use a variety of algorithms to determine the color of individual pixels efficiently.
    :param n_points:
    :param max_iterations:
    :return:
    """
    pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
    infinity_border = 100
    image = np.zeros((n_points, n_points))
    for ip, p in enumerate(np.linspace(pmin, pmax, n_points)):
        for iq, q in enumerate(np.linspace(qmin, qmax, n_points)):
            c = p + 1j * q
            z = 0
            for k in range(max_iterations):
                z = z ** 2 + c
                if abs(z) > infinity_border:
                    image[ip, iq] = 1
                    break
    return image