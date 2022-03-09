'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_dict:
                return [i, nums_dict[target - nums[i]]]
            else:
                nums_dict[nums[i]] = i
        return []

    # def towSumV2(self, nums, target):
    #     left, right = 0, len(nums) - 1
    #     nums = sorted(nums)
    #     while left < right:
    #         sum = nums[left] + nums[right]
    #         if sum > target:
    #             right -= 1
    #         elif sum < target:
    #             left += 1
    #         else:
    #             return [left, right]
    #     return []

if __name__ == "__main__":
    solution = Solution()
    print(solution.towSumV2([3,2,4], 6))
