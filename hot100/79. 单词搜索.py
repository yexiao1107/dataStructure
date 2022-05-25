'''
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例 1：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
示例 3：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false

'''


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n, m = len(board), len(board[0])

        def dfs(board, x, y, word):
            if not word:
                return True
            if 0 <= x < n and 0 <= y < m and board[x][y] == word[0] and board[x][y] != '#':
                t, board[x][y] = board[x][y], '#'
                res = dfs(board, x, y + 1, word[1:]) or \
                      dfs(board, x, y - 1, word[1:]) or \
                      dfs(board, x + 1, y, word[1:]) or \
                      dfs(board, x - 1, y, word[1:])
                board[x][y] = t
                return res

            return False

        for i in range(n):
            for j in range(m):
                if dfs(board, i, j, word):
                    return True
        return False
