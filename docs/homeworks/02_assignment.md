# Assignment 2 (8 p.)

In this assignment you have to develop metadata proccesor fot STEM Framework.

Meta is tree-like structure which on top level contains key-value pairs: key is string, value is primitive type, list or another Meta type.

Specification is description of mandatory part meta data which must be present in Meta for given task and before execution task metadata processor checked what given meta complies specififcation.

1. (1 p.) In `core.py` module create protocol `Dataclass` as type annotations for dataclass object.
2. (1 p.) In `meta.py` module create type annotations for next type:
   1. `Meta` --- union `dict` and `Dataclass` type.
   2. Specification field type `SpecificationField` --- pairs of necessary meta key and necessary meta value type (or types, or another specification if meta value is another `Meta`)
   3. `Specification` for specification --- union of `Dataclass` or tuple of `SpecifiationField` type.
   Note: if necessary we can add additional type annotation 
3. (1 p.) Implement function `get_meta_attr(meta : Meta, key : str, default : Optional[Any] = None) -> Optional[Any]:` which return meta value by `key` from top level of `meta` or `default` if `key` don't exist in `meta`.
4. (1 p.) Implement function `def update_meta(meta: Meta, **kwargs):` which update `meta` from `kwargs`.
5. (4 p.) Implement class `MetaVerification`
