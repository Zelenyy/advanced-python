# Assignment 11 (p.)

In this assignment you have to implement a middleware server which 
provide access to computation server and distribute tasks between their.

1. Implement next methods for class `Envelope`:
   1. (1 p.) `async def async_read(reader: StreamReader) -> "Envelope":`
   2. (1 p.) `async def async_write_to(self, writer: StreamWriter):`
2. (8? p.) Implement class `Distributor`
3. (1 p.) Implement method `start_distributor(host: str, port: int, servers: list[tuple[str, int]])` which using module `asyncio` run asynchronous TCP server. For request handling use class `Distributor` from previous task.
4. (1 p.) Implement method `start_distributor_in_subprocess(host: str, port: int, servers: list[tuple[str, int]]) -> Process` which using method `start_distributor` run TCP server in children process.