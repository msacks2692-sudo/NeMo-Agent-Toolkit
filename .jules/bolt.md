# Bolt's Journal

## 2024-05-22 - [Optimizing DecomposedType Instantiation]
**Learning:** `DecomposedType` wrapper around `type` objects is instantiated frequently in `TypeConverter`, causing redundant computations despite `lru_cache` on properties, because the instance itself is recreated.
**Action:** Use `__new__` and `lru_cache` to cache `DecomposedType` instances based on the input type.
