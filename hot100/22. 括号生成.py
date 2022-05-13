'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]

'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def backtrack(left, right, track):
            if left > right: return
            if left < 0 or right < 0: return
            if left == 0 and right == 0:
                res.append("".join(track))
                return
            track.append("(")
            backtrack(left - 1, right, track)
            track.pop()

            track.append(")")
            backtrack(left, right - 1, track)
            track.pop()

        res = []
        track = []
        backtrack(n, n, track)
        return res