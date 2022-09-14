# Assignment 2 (12 p.)

In this assignment you have to develop metadata processor for STEM Framework.

In STEM, task run include three stage:

1. Resolving of task dependencies and building task tree.
2. Meta data verification: each task have `Specification` which describe required meta and meta data processor check input meta on accordance specification.
3. Invocation of ech task.

Meta is tree-like structure which on top level contains key-value pairs: key is string, value is primitive type, list or another Meta type. In STEM we will use dictionary and dataclass as Meta object.

Specification is description of mandatory part metadata which must be present in Meta for given task and before execution task metadata processor checked what given meta complies specification. In STEM we will use dataclass class-object if dataclass using as Meta object and sequence of name-type pairs in another case.

1. (1 p.) In `core.py` module create protocol `Dataclass` as type annotations for dataclass object.
2. (1 p.) In `meta.py` module create type annotations for next type:
   1. `Meta` --- union `dict` and `Dataclass` type.
   2. Specification field type `SpecificationField` --- pairs of necessary meta key and necessary meta value type (this can be single type, tuple of types, or another specification if meta value is another `Meta`)
   3. `Specification` for specification --- union of `Dataclass` or tuple of `SpecifiationField` type.
   Note: if necessary we can add additional type annotation 
3. (1 p.) In `meta.py` module implement function `get_meta_attr(meta : Meta, key : str, default : Optional[Any] = None) -> Optional[Any]:` which return meta value by `key` from top level of `meta` or `default` if `key` don't exist in `meta`.
4. (1 p.) In `meta.py` module implement function `def update_meta(meta: Meta, **kwargs):` which update `meta` from `kwargs`.
5. (6 p.) In `meta.py` module implement class `MetaVerification` --- this class contains result of meta verification, in field `errors` contains list of instance of dataclass  `MetaFieldError` or another `MetaVerification`:
   1. Implement _property_ `checked_success`, return `True` if  not errors of verification.
   2. Implement _staticmethod_ `def verify(meta: Meta, specification: Optional[Specification] = None) -> "MetaVerification":` which verify `meta` by `specification`. Raise `SpecificationError` if verification impossible.
6. (2 p.) In `core.py` module implement class `Named` with _property_ `name`: this property return value of private variable `_name` if it is not None and return name of current class (Named or his children) in snake_case (for translation classname from PascalCase to snake_case implement `def pascal_case_to_snake_case(name: str) -> str:` function)
