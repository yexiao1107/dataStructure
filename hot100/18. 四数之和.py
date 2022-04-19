'''
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

 

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：

输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
 

提示：

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def nSum(nums, n, start, target):
            sz = len(nums)
            res = []
            if n < 2 or n > sz:
                return res

            if n == 2:
                low, high = start, sz - 1
                while low < high:
                    left, right = nums[low], nums[high]
                    s = left + right
                    if s == target:
                        res.append([left, right])
                        while low < high and nums[low] == left: low += 1
                        while low < high and nums[high] == right: high -= 1
                    elif s < target:
                        while low < high and nums[low] == left: low += 1
                    else:
                        while low < high and nums[high] == right: high -= 1
            else:
                i = start
                while i < sz:
                    sub = nSum(nums, n - 1, i + 1, target - nums[i])
                    for r in sub:
                        r.append(nums[i])
                        res.append(r)
                    while i < len(nums) - 1 and nums[i] == nums[i + 1]: i += 1
                    i += 1
        nums = sorted(nums)
        return nSum(nums, 4, 0, target)