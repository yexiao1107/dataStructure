'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]
 

提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def twoSum(nums, start, target):
            res = []
            low, high = start, len(nums) - 1
            while low < high:
                left, right = nums[low], nums[high]
                sum_res = left + right
                if sum_res < target:
                    while low < high and nums[low] == left: low += 1
                elif sum_res > target:
                    while low < high and nums[high] == right: high -= 1
                else:
                    res.append([left, right])
                    while low < high and nums[low] == left: low += 1
                    while low < high and nums[high] == right: high -= 1
            return res

        res = []
        nums = sorted(nums)
        i = 0
        while i < len(nums):
            tmp = twoSum(nums, i + 1, 0 - nums[i])
            for item in tmp:
                item.append(nums[i])
                res.append(item)
            while i < len(nums) - 1 and nums[i] == nums[i + 1]: i += 1
            i += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
