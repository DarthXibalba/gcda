def remove_duplicates_from_sorted_array(sorted_nums: list[int]) -> int:
    i = 0 
    if len(sorted_nums) > 1:
        j = i + 1
        while j < len(sorted_nums):
            if sorted_nums[i] == sorted_nums[j]:
                j += 1
            else:
                i += 1
                sorted_nums[i] = sorted_nums[j]

    return i + 1
