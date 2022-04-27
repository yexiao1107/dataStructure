'''
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 

示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        uper, left, right, lower = 0, 0, n - 1, n - 1
        matrix = [[0] * n for _ in range(n)]
        num = 1
        while num <= n * n:
            ##上界左到右
            for j in range(left, right + 1):
                matrix[uper][j] = num
                num += 1
            uper += 1

            for i in range(uper, lower + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            for j in range(right, left - 1, -1):
                matrix[lower][j] = num
                num += 1
            lower -= 1

            for i in range(lower, uper - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix
