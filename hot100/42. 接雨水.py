'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
 

提示：

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''


class Solution(object):
    def trap1(self, height):
        '''
        暴力解法，超时，算max时计算自己，最高就是0
        '''
        res = 0
        for i in range(1, len(height) - 1):
            l_max, r_max = max(height[:i + 1]), max(height[i:])
            res += min(l_max, r_max) - height[i]
        return res

    def trap2(self, height):
        '''
        备忘录，提前计算max
        '''
        n = len(height)
        l_max = [0] * n
        l_max[0] = height[0]
        r_max = [0] * n
        r_max[-1] = height[-1]
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i - 1])
        for i in range(n - 2, -1, -1):
            r_max[i] = max(height[i], r_max[i + 1])
        res = 0
        for i in range(1, n - 1):
            res += min(l_max[i], r_max[i]) - height[i]
        return res

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        l_max, r_max = 0, 0
        res = 0
        while left < right:
            l_max = max(height[left], l_max)
            r_max = max(height[right], r_max)

            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.trap1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
