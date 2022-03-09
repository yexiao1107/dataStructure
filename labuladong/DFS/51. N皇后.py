'''
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]
 

提示：

1 <= n <= 9
'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def is_vaild(track, row, col):
            ##检查同一列的是否有冲突
            for i in range(len(track)):
                if track[i][col] == "Q": return False
            ##检查右上方
            i, j = row - 1, col + 1
            while i >= 0 and j < len(track):
                if track[i][j] == "Q": return False
                i -= 1
                j += 1
            ##检查左上方
            m, n = row - 1, col - 1
            while m >= 0 and n >= 0:
                if track[m][n] == "Q": return False
                m -= 1
                n -= 1
            return True

        def backtrack(track, row):
            if n == row:
                temp_res = []
                for temp in track:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)

            for col in range(n):
                ##做选择
                if not is_vaild(track, row, col): continue
                track[row][col] = "Q"
                backtrack(track, row + 1)
                track[row][col] = "."

        res = []
        track = [['.'] * n for _ in range(n)]
        backtrack(track, 0)
        return res
if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(4))
