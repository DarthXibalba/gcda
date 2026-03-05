def rotate_array(nums, k):
    n = len(nums)
    kmod = k % n
    reverse_array(nums, 0, n-1)
    reverse_array(nums, 0, kmod-1)
    reverse_array(nums, kmod, n-1)

def reverse_array(nums, bound1, bound2):
    while bound1 < bound2:
        tmp = nums[bound1]
        nums[bound1] = nums[bound2]
        nums[bound2] = tmp
        bound1 += 1
        bound2 -= 1
