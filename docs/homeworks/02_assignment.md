# Assignment 2 (12 p.)

In this assignment you have to develop a metadata processor for the STEM Framework.

In the STEM, the task run includes three stage:

1. Resolving the task dependencies and building the task tree.
2. Metadata verification: each task has `Specification` which describes required meta and the metadata processor checks input meta the correspondence to the specification.
3. The invocation of each task.

Meta is tree-like structure which contains key-value pairs on top level. The key is a string, the value is a primitive type, list or another Meta type. In the STEM we will use a dictionary and a dataclass as Meta objects.

Specification is description of mandatory part of the metadata which must be present in the Meta for the given task. The metadata processor checks whether the given meta corresponds specification before the execution of the task. In the STEM we use dataclass class-object if the dataclass instance is used as the Meta object and sequence of name-type pairs otherwise.

1. (1 p.) In `core.py` module create a protocol `Dataclass` as a type annotation for a dataclass object.
2. (1 p.) In `meta.py` module create a type annotation for the next types:
   1. `Meta` --- union of the `dict` and the `Dataclass` type.
   2. Specification field type `SpecificationField` --- pairs of necessary meta key and necessary meta value type (this can be single type, tuple of types, or another specification if meta value is another `Meta`)
   3. `Specification` for specification --- union of the `Dataclass` or tuple of the `SpecifiationField` type.
   Note: we can add additional type annotations if necessary. 
3. (1 p.) In `meta.py` module implement function `get_meta_attr(meta : Meta, key : str, default : Optional[Any] = None) -> Optional[Any]:` which return meta value by `key` from top level of `meta` or `default` if `key` don't exist in `meta`.
4. (1 p.) In `meta.py` module implement function `def update_meta(meta: Meta, **kwargs):` which update `meta` from `kwargs`.
5. (6 p.) In `meta.py` module implement class `MetaVerification` --- this class contains result of meta verification. It contains list of instance of dataclass `MetaFieldError` or another `MetaVerification` in the field `errors`:
   1. Implement _property_ `checked_success` that returns `True` if there is no errors of verification.
   2. Implement _staticmethod_ `def verify(meta: Meta, specification: Optional[Specification] = None) -> "MetaVerification":` which verify `meta` by `specification`. Raise `SpecificationError` if verification impossible.
6. (2 p.) In `core.py` module implement class `Named` with _property_ `name`. This property returns value of private variable `_name` if it is not None and returns name of current class (`Named` or his children) in snake_case (for translation classname from PascalCase to snake_case implement `def pascal_case_to_snake_case(name: str) -> str:` function).
