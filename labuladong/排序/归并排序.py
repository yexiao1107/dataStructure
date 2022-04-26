def sort(nums):
    def merge(left, right):
        res = []
        i, j = 0, 0
        while i <= len(left) and j <= len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
        return res

    if len(nums) < 2: return nums
    mid = len(nums) // 2
    left = sort(nums[:mid])
    right = sort(nums[mid:])
    return merge(left, right)
