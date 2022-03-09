'''
给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。

返回 A 的任意排列，使其相对于 B 的优势最大化。

 

示例 1：

输入：A = [2,7,11,15], B = [1,10,4,11]
输出：[2,11,7,15]
示例 2：

输入：A = [12,24,8,32], B = [13,25,32,11]
输出：[24,32,8,12]
 

提示：

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
'''


class Solution:
    def advantageCount(self, nums1: [int], nums2: [int]) -> [int]:
        sort_nums1 = sorted(nums1)  ##nums1排序，从小到大
        sort_nums2_index = sorted(range(len(nums2)), key=lambda k: nums2[k])  ##nums2仅获取index, 不能改变顺序，输出结果还需要nums2顺序
        res = [0] * len(nums1)
        left, right = 0, len(nums1) - 1
        for i in range(len(nums1)):
            index = sort_nums2_index.pop()
            max_val = nums2[index]
            if sort_nums1[right] > max_val:
                res[index] = sort_nums1[right]
                right -= 1
            else:
                res[index] = sort_nums1[left]
                left += 1
        return res

    def advantageCountV2(self, nums1: [int], nums2: [int]) -> [int]:
        from queue import PriorityQueue
        pq = PriorityQueue()
        for i, item in enumerate(nums2):
            pq.put((-item, i))
        '''
        利用二叉堆实现nums的从大到小排序，并记录index, 结果输出需要nums2的原始顺序
        python不建议
        '''
        sort_nums1 = sorted(nums1)  ##nums1排序，从小到大
        res = [0] * len(nums1)
        left, right = 0, len(nums1) - 1
        while not pq.empty():
            value = pq.get()
            index, max_val = value[1], -value[0]
            if sort_nums1[right] > max_val:
                res[index] = sort_nums1[right]
                right -= 1
            else:
                res[index] = sort_nums1[left]
                left += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.advantageCountV2([12, 24, 8, 32], [13, 25, 32, 11]))
