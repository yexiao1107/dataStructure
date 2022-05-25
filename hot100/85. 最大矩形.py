'''
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

 

示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = []
输出：0
示例 3：

输入：matrix = [["0"]]
输出：0
示例 4：

输入：matrix = [["1"]]
输出：1
示例 5：

输入：matrix = [["0","0"]]
输出：0
'''
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def maxArea(heights):
            res = 0
            heights.append(-1)
            stack = [-1]
            for idx, val in enumerate(heights):
                while heights[stack[-1]] > val:
                    h = heights[stack.pop()]
                    res = max(res, h * (idx - stack[-1] - 1))
                stack.append(idx)
            return res

        m, n = len(matrix), len(matrix[0])
        h = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    h[j] += 1
                else:
                    h[j] = 0
            res = max(res, maxArea(h))
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximalRectangle([["0","1"],["1","0"]]))