'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

 

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
 

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        need, window = {}, {}
        for c in t: need[c] = need.get(c, 0) + 1
        vaild = 0
        start, length = 0, len(s) + 1
        while (right < len(s)):
            ##窗口右移
            c = s[right]
            right += 1
            if (c in need):
                ##need中没有可以不用判断
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    vaild += 1
            while vaild == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        vaild -= 1
                    window[d] = window.get(d) - 1
        return "" if length == len(s) + 1 else s[start:start + length]
