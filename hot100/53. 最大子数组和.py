'''
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_sums = [0] * (len(nums) + 1)
        ##前缀和
        for i in range(1, len(pre_sums)):
            pre_sums[i] = pre_sums[i - 1] + nums[i - 1]
        res = float("-inf")
        min_val = float("inf")
        ##pre_sum - 前缀和最小的和即最大和
        for i in range(len(nums)):
            min_val = min(min_val, pre_sums[i])
            res = max(res, pre_sums[i + 1] - min_val) ## i的最大和
        return res