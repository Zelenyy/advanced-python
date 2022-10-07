# Assignment 4 (14 p.)

In this assignment you have to implement building the task tree and automatically dependence resolving.

In the STEM, tasks union in special workspaces (which implemented as children of interface `IWorkspace` and can have sub-workspaces). Also, tasks can be defined on module level and in this case, its implicitly union to special module-workspaces. 


1. (8 p.) Implement **metaclass** `Workspace(ABCMeta, ILocalWorkspace):` in module `workspace.py`. This metaclass provides next features for user classes:
   1. The class-object itself must be returned on constructor call of user classes.
   2. Class-objects of user classes implement the interface `ILocalWorkspace` (see inheritance of `Workspace` class).
   3. All attributes (not methods) of the user workspace class, which inherit the class `Task` must be replaced on `ProxyTask` objects, using as attribute/method names as proxy names (The constructor of class `ProxyTask` receive two arguments: some task object and it proxy name).
   4. All `ProxyTask` attributes and methods (which inherit the class `Task` objects) of the user workspace class must be accessible from property `tasks` (Property `tasks` return dictionary, which have names of tasks in keys and itself tasks in values).
   5. All tasks (`ProxyTask` attributes and task-methods) must have the attribute `_stem_workspace` which contain this workspace.
   6. Attribute `workspaces` of the user workspace class must be converted to set if present else property `workspaces` must be return empty set (Property `workspaces` return set contains sub-workspaces of this workspace).
   Note: Metaclass is black magic, we can ignore ordinary rules of object creation.
2. (2 p.) In module `workspace.py`, in class `IWorkspace` implement method  `find_task(self, task_path: Union[str, TaskPath]) -> Optional[Task]` which return task from this workspace or from his sub-workspaces. `task_path` is special `TaskPath` object or string in next format: names of sub-workspaces (can be no one) and the name of task joined by `"."`. If `task_path` contains only task name and task with this name absent in workspace should proceed search in sub-workspaces. Return `None` if task can't be found.
3. (3 p.) In module `workspace.py`, in class `IWorkspace` implement **staticmethod**  `module_workspace(module: ModuleType) -> "IWorkspace"` which return module-workspaces. Module-workspaces is the instance of the class `LocalWorkspace`, which contain tasks (instance of class `Task` or its subclasses) and workspaces (instance of class `IWorkspace` and its subclasses) defined in module associated with variable `module`. Module-workspace is contained in module variable `__stem_workspace` if this variable exists, otherwise you should create it and store it in this variable.
4. (1 p.) In module `workspace.py`, in class `IWorkspace` implement **staticmethod** `find_default_workspace(task: Task) -> "IWorkspace"`. This method return `_stem_workspace` value if it exists and module-workspace for module which contains task definition.

