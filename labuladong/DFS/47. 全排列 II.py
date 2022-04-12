'''
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(nums):
            if len(track) == len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if used[i]: continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue
                track.append(nums[i])
                used[i] = True
                backtrack(nums)
                used[i] = False
                track.pop()

        nums = sorted(nums)
        res = []
        track = []
        used = [False] * len(nums)
        backtrack(nums)
        return res
