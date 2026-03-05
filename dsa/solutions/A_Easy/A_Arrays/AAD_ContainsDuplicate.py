def contains_duplicate_using_dict(nums: list[int]) -> bool:
    seen = {}
    for n in nums:
        if n in seen:
            return True
        seen[n] = True
    return False

def contains_duplicate_using_set(nums: list[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

def contains_duplicate_sort(nums: list[int]) -> bool:
    nums = sorted(nums)          # or nums.sort() if you can mutate input
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

def contains_duplicate_stream(iterable: iter) -> bool:
    seen = set()
    for x in iterable:
        if x in seen:
            return True
        seen.add(x)
    return False

def contains_duplicate_bitset(nums: list[int], max_value: int) -> bool:
    bitset = 0
    for n in nums:
        if n < 0 or n > max_value:
            raise ValueError(f"Value {n} out of range [0, {max_value}]")
        if (bitset >> n) & 1:
            return True
        bitset |= (1 << n)
    return False
