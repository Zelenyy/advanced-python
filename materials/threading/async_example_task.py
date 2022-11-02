import asyncio
import time


async def say_after(delay, what, base_time):
    await asyncio.sleep(delay)
    print((time.perf_counter_ns() - base_time)//1_000, what, flush=True)

async def main():
    base_time = time.perf_counter_ns()
    task1 = asyncio.create_task(
        say_after(1, 'hello', base_time))

    task2 = asyncio.create_task(
        say_after(2, 'world', base_time))

    print(0)

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    # print((time.perf_counter_ns() - base_time)//1_000)
    await task2

    print((time.perf_counter_ns() - base_time)//1_000)

if __name__ == '__main__':
    asyncio.run(main())