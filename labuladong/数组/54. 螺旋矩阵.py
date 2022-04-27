'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

 

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        uper, left, right, lower = 0, 0, n - 1, m - 1
        res = []
        while len(res) < m * n:
            if uper <= lower:
                ##上界左到右
                for j in range(left, right + 1):
                    res.append(matrix[uper][j])
                uper += 1

            if left <= right:
                for i in range(uper, lower + 1):
                    res.append(matrix[i][right])
                right -= 1

            if uper <= lower:
                for j in range(right, left - 1, -1):
                    res.append(matrix[lower][j])
                lower -= 1

            if left <= right:
                for i in range(lower, uper - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))