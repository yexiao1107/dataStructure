'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
 

提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
'''


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(nums, track):
            if (len(track) == len(nums)):
                res.append(track[:])##深拷贝
                return

            for item in nums:
                if item in track: continue
                track.append(item)
                backtrack(nums, track)
                track.pop()

        res = []
        stack = []
        backtrack(nums, stack)
        return res



if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1, 2, 3]))


