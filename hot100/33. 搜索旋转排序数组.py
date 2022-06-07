'''
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

 

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        若 target == nums[mid]，直接返回
        若 nums[left] <= nums[mid]，说明左侧区间 [left,mid]「连续递增」。此时：
        若 nums[left] <= target < nums[mid]，说明 target 位于左侧。令 right = mid-1，在左侧区间查找
        否则，令 left = mid+1，在右侧区间查找
        否则，说明右侧区间 [mid,right]「连续递增」。此时：
        若 nums[mid] < target <= nums[right]，说明 target 位于右侧区间。令 left = mid+1，在右侧区间查找
        否则，令 right = mid-1，在左侧区间查找
        注意：区间收缩时不包含 mid，也就是说，实际收缩后的区间是 [left,mid) 或者 (mid,right]

        将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
        此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
