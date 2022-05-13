'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 

 

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        infinty = 2 ** 40
        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            # 前一部分包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
            # // 后一部分包含 nums1[i .. m-1] 和 nums2[j .. n-1]
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            max_leftA = (-infinty if i == 0 else nums1[i - 1])
            min_rightA = (infinty if i == m else nums1[i])
            max_leftB = (-infinty if j == 0 else nums2[j - 1])
            min_rightB = (infinty if j == n else nums2[j])

            if max_leftA <= min_rightB and min_rightA >= max_leftB:
                if (m + n) % 2 != 0:
                    return max(max_leftA, max_leftB)
                else:
                    return (max(max_leftA, max_leftB) + min(min_rightA, min_rightB)) / 2.0
            elif max_leftA > min_rightB:
                right = i - 1
            else:
                left = i + 1
        return 0.0
