## 2025-02-13 - [Avoid O(N) dict keys conversion for first element]
**Learning:** Using `list(my_dict.keys())[0]` to get the first key of a dictionary forces Python to allocate a new list and iterate over all keys, making it an O(N) operation.
**Action:** Replace `list(my_dict.keys())[0]` with `next(iter(my_dict))` which is an O(1) operation and avoids memory allocation, yielding ~10x performance improvement.
