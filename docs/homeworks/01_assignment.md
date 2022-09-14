# Assignment 1 (8 p.)

In this assignment you have to prepare your project workspace.
In during semester, we will develop two projects: STEM framework and Super TEmperature Monitor.

1. (1 p.) Create git repository for your project in Space ([project "Advanced Python"](https://mipt-npm.jetbrains.space/p/advanced-python-2021)) or on Github, and send me link on repository. Merge top commit of main branch from [this repository](https://github.com/Zelenyy/advanced-python-homework) in your repository.
2. (1 p.) Create two directory (every directory used for single project: `stem_framework` and `temperature_monitor`, in both directory create python package `stem` and file `setup.py`. 
3. (1 p.) Create license for both projects.

**Next tasks performed in project STEM framework (directory `stem_framework`).**

4. (1 p.) Create file for deployment virtual enviroment (using `venv`, `virtualenv` or `condaenv`). Add command for deployment in project `README.md`. Virtual environment must be contained package necessary for develop project (not project dependency), namely Sphinx, Pylint and MyPy. 
5. (1 p.) Fill `setup.py` file for setuping `stem` package in developer mode.
6. (1 p.) Read paper [DataForge: Modular platform for data storage and analysis](http://dx.doi.org/10.1051/epjconf/201817705003).
7. (1 p.) Add next modules in `stem` package: `core.py`, `meta.py`, `task.py`, `workspace.py`. Add shortly module level docstring in modules `meta.py`, `task.py`, `workspace.py`. In `meta.py` docstring describe conception of metadata and metadata processor. In `task.py` describe task terms, in `workspace.py` conception modularity software.
8. (1 p.) Create Sphinx documentation of `stem` package (include docstrings of `stem` package). Add to repository configs for build documentation. Make integration between sphinx and `setup.py`, allow build documentation using `python setup.py build_sphinx`.
