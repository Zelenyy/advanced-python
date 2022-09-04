# Assignment 10 (10? p.)

In this assignment you have to implement server side of remote workspace: create TCP server and handler allow send information about accessible tasks and run task in server workspace.

1. (8? p.) Implement class `UnitHander(StreamRequestHandler)`
2. (1 p.) Implement method `start_unit(workspace: IWorkspace, host: str, port: int, powerfullity: Optional[int] = None)` which run TCP server able handle every request in own thread. For request handling use class `UnitHander(StreamRequestHandler)` from previous task.
3. (1 p.) Implement method `start_unit_in_subprocess(workspace: IWorkspace, host: str, port: int, powerfullity: Optional[int] = None) -> Process:` which using method `start_unit` run TCP server in children process.