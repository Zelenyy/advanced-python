import time


def mandelbrot():
    pmin, pmax, qmin, qmax = -250, 150, -200, 200
    ppoints, qpoints = 200, 200
    max_iterations = 400
    infinity_border = 100
    image = [[0 for i in range(qmax - qmin)] for j in range(pmax-pmin)]
    for ip, p in enumerate(range(pmin, pmax)):
        for iq, q in enumerate(range(qmin, qmax)):
            c = p + 1j * q
            z = 0
            for k in range(max_iterations):
                z = z ** 2 + c
                if abs(z) > infinity_border:
                    image[ip][iq] = 1
                    break
    return image

if __name__ == '__main__':
    tic = time.perf_counter_ns()
    image = mandelbrot()
    toc = time.perf_counter_ns()
    print((toc - tic)/1_000_000_000, "s")
    # plt.imshow(image)
    # plt.show()