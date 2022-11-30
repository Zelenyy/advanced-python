# Assignment 14 (12 p.)

In this assignment you continue to develop of STEM: Serious TEmperature Monitor --- application with GUI, which allow measure temperature using USB thermometer, save results in database and present graph of the temperature.

1. (2 p.) In the module `config.py` implement the function `from_dict(data: dict, factory: Type[T]) -> T` which create dataclass instance of type `factory` (guaranteed what `factory` is dataclass type) from dict **in take to account** what type `factory` can be has another dataclass as field and its also can be created from nested dictionary entry.
2. (2 p.) In the module `config.py` implement the function `resolve_config(factory: Type[T], user_path: Union[str,Path], default_path : Union[str,Path]) -> T` which create dataclass instance of type `factory` (guaranteed what `factory` is dataclass type) from user/default config in YAML format (see `config.yaml`) by  next algorithm:
   1. If `user_path` path exist than created from it.
   2. If `user_path` path don't exist than check `dafult_path` path.
   3. If `default_path` path exist than created from it.
   4. If `default_path` path don't exist than created dataclass with default field (its garuanted) and **save this config to `default_path` in YAML format**.
3. (1 p.) In the module `app.py` fixe the call of `resolve_config` in the function `run`. Add as `default_path` path to default user system directory for application config (used module `appdirs`, application name is `STEM`, application author is you username).
4. (1 p.) In the module `database.py` implement the class `Point` which describe table with two columns: temperature value and time of measurement (database usually have special types for datetime data).
5. (4 p.) In the module `database.py` implement the class `Database` with next methods:
   1. `add_point(self, point: Point)` --- insert point to database.
   2. `get_points(self, from_date: datetime) -> list[Point]` --- get list of point from given date.
   3. **staticmethod** `create_or_connect_sqlite(config: SqliteConfig) -> "Database"` create of `Database` instance with connect (or create and connect) to sqlite database with parameters from `config`.
   4. `__init__(self, engine: Engine):` --- create the table `Point` in database `engine`
6. (2 p.) Connect `Database` instance from `run` function to your application: autosave measured temperature and time of measurement in database, as well as on application start load on plot all points from last 15 minutes.