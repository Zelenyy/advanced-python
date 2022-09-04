# Assignment 9 (12? p.)

In this assignment you have to implement several inheritor of class `TaskRunner`.

1. (4 p.) Using module `threading` implement class `ThreadingRunner`, which execute every task in own thread. Use `MAX_WORKERS` class field as maximum number of threads that can be used to execute.
2. (4 p.) Using module `asyncio` implement class `AsyncRunner`, which execute every task in own coroutine.
3. (4? p.) Using module `multyprocessing` implement class `ProcessingRunner`, which execute every task in own process. Use `MAX_WORKERS` class field as maximum number of processes that can be used to execute.