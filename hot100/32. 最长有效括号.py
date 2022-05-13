'''
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    left_index = stack.pop()
                    l = 1 + i - left_index + dp[left_index]
                    dp[i + 1] = l
        return max(dp)