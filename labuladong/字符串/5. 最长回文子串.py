'''
给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def palindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        res = ""
        for i in range(len(s)):
            res1 = palindrome(s, i, i)
            res2 = palindrome(s, i, i + 1)
            res = res1 if len(res1) > len(res) else res
            res = res2 if len(res2) > len(res) else res
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("abba"))
