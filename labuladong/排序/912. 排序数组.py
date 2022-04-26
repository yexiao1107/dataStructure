'''
给你一个整数数组 nums，请你将该数组升序排列。

 

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
'''
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result += left[i:]
            result += right[j:]
            return result

        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2  # 将列表分成更小的两个列表
        # 分别对左右两个列表进行处理，分别返回两个排序好的列表
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        # 对排序好的两个列表合并，产生一个新的排序好的列表
        return merge(left, right)