def sort(nums, i, j):
    if i >= j: return nums
    pvi = nums[i]
    low, high = i, j
    while i < j:
        while i < j and nums[j] >= pvi:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= pvi:
            i += 1
        nums[j] = nums[i]
    nums[j] = pvi
    sort(nums, low, i - 1)
    sort(nums, i + 1, high)
    return nums
