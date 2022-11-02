import time
import asyncio
from async_mandelbrot import mandelbrot



async def task(name):
    for i in range(5):
        await mandelbrot()
        await asyncio.sleep(3)
        print("Task {}, iteration {}".format(name, i), flush=True)

async def main():
    tic = time.perf_counter()
    pool = []
    for i in range(5):
        pool.append(task("task_{}".format(i)))
    await asyncio.gather(*pool)
    toc = time.perf_counter()
    print(toc - tic, "s")
    return 0

if __name__ == '__main__':
    asyncio.run(main())