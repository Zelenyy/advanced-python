# Assignment 10 (14 p.)

In this assignment you have to implement client and server side of remote workspace: create TCP server and handler allow send information about accessible tasks and run task in server workspace.

1. (6 p.) In module `remote.unit.py` implement the class `UnitHander(StreamRequestHandler)` which have access to some workspace, task tree and task master. Class `UnitHandler` get user request in Dataforge Envelope (see assigment 7) and return answer also in envelope format. Class `UnitHandler` must be implement next protocol:
   1. In input request contains message in envelope format. In message metadata block contains entries with key `command`. If input request don't contain envelope message or envelope message don't contain key `command` should send envelope answer with next meta entries:
      1. Entry with key `status` and value `failed`.
      2. Entry with key `error` and value contains information about error (exception message as example)
   2. If key `command` is presented in message, invoke next action and send result in envelope format:
      1. If `command="run"`, check entry with key `task_path` in metadata and if present run this task. Result of task executing return as envelope.
      2. If `command="structure"`, return envelope with workspace structure (use method `structure` of workspace).
      3. If `command="powerfullity"`, return envelope with meta entry ``powerfullity` which contains some number constant.
2. (1 p.) In module `remote.unit.py` implement the method `start_unit(workspace: IWorkspace, host: str, port: int, powerfullity: Optional[int] = None)` which run TCP server able handle every request in own thread. For request handling use class `UnitHander(StreamRequestHandler)` from previous task.
3. (1 p.) In module `remote.unit.py` implement the method `start_unit_in_subprocess(workspace: IWorkspace, host: str, port: int, powerfullity: Optional[int] = None) -> Process:` which using method `start_unit` run TCP server in children process.
4. (4 p.) In module `remote.remote_workspace.py` implement the class `RemoteWorkspace(IWorkspace)` which connect to remote TCP server implemented in task 1-2.
4. (2 p.) In module `remote.remote_workspace.py` implement the class `RemoteTask(Task)` which connect to remote TCP server implemented in task 1-2.