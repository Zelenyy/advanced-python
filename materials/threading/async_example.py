import asyncio
import time

async def say_after(delay, what, base_time):
    await asyncio.sleep(delay)
    print((time.perf_counter_ns() - base_time)//1_000, what, flush=True)

async def main():
    base_time = time.perf_counter_ns()
    print(0, flush=True)

    await say_after(1, 'hello', base_time)
    print((time.perf_counter_ns() - base_time)//1_000, flush=True)
    await say_after(2, 'world', base_time)

    print((time.perf_counter_ns() - base_time)//1_000)

if __name__ == '__main__':
    asyncio.run(main())