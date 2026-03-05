def two_sum(nums: list[int], target: int) -> tuple[int]:
    seen = {}
    for i, n in enumerate(nums):
        if n in seen:
            return (seen[n], i)
        else:
            seen[target-n] = i
    return (-1, -1)
