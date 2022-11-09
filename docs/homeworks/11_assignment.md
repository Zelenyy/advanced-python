# Assignment 11 (8 p.)

In this assignment you have to implement a middleware server which 
provide access to computation server and distribute tasks between their.

1. Implement next methods for class `Envelope`:
   1. (1 p.) `async def async_read(reader: StreamReader) -> "Envelope":`
   2. (1 p.) `async def async_write_to(self, writer: StreamWriter):`
2. (4 p.) In module `remote.distributor.py` implement the class `Distributor` which provide access to units server (see assigment 10) and another distributor servers.  Class `Distributor` get user request in Dataforge Envelope (see assigment 7) and return answer also in envelope format. Class `Distributor` must be implemented next protocol:
   1. In input request contains message in envelope format. In message metadata block contains entries with key `command`. If input request don't contain envelope message or envelope message don't contain key `command` should send envelope answer with next meta entries:
      1. Entry with key `status` and value `failed`.
      2. Entry with key `error` and value contains information about error (exception message as example)
   2. If key `command` is presented in message, invoke next action and send result in envelope format:
      1. If `command="run"`, check entry with key `task_path` in metadata and if present select random child server (with weight by powerfullity) and run this task on selected child server. Result of task executing return as envelope.
      2. If `command="structure"`, return envelope with workspace structure of child server.
      3. If `command="powerfullity"`, return envelope with meta entry `powerfullity` which contains sum of child server `powerfullity`.
3. (1 p.) In module `remote.distributor.py` implement the method `start_distributor(host: str, port: int, servers: list[tuple[str, int]])` which using module `asyncio` run asynchronous TCP server. For request handling use class `Distributor` from previous task.
4. (1 p.) In module `remote.distributor.py` implement the method `start_distributor_in_subprocess(host: str, port: int, servers: list[tuple[str, int]]) -> Process` which using method `start_distributor` run TCP server in children process.