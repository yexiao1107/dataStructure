'''
给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。

 

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2
 

提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''


class Solution:
    '''
    前缀和解题，暴力解法可能超时
    '''

    def subarraySum(self, nums: [int], k: int) -> int:
        '''
        该解法最为直接，但是会超时
        '''
        pre_sum = [0] * (len(nums) + 1)
        for i in range(1, len(pre_sum)):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        res = 0
        for i in range(1, len(pre_sum)):
            for j in range(0, i):
                if pre_sum[i] - pre_sum[j] == k:
                    res += 1
        return res

    def subarraySumV2(self, nums: [int], k: int) -> int:
        '''
        利用dict记录每一组的前缀和的个数，p[i]为（0，i）前缀和，p(i) = p(i-1) + nums(i)
        (j,i)的前缀和即p(i)-p(j-1), 找到（j,i）内前缀和为k的个数，以 i 结尾的和为 k 的连
        续子数组个数时只要统计有多少个前缀和p(i)-k的个数即可
        '''
        res = 0
        pre_sum_dict = {0: 1}
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum = pre_sum + nums[i]
            sum = pre_sum - k
            if sum in pre_sum_dict:
                res += pre_sum_dict[sum]
            pre_sum_dict[pre_sum] = pre_sum_dict.get(pre_sum, 0) + 1
        print(pre_sum_dict)
        return res

if __name__=="__main__":
    solution = Solution()
    print(solution.subarraySumV2([1, 1, 1], 2))
