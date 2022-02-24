'''
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

 

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

提示：

1 <= s.length <= 104
s 由小写英文字母组成
'''


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}
        for item in s:
            count[item] = count[item] + 1 if item in count else 1
        stack = []
        flag = {}
        for item in s:
            count[item] -= 1
            if flag.get(item, False): continue
            ##字典序比前边的小，则pop
            while stack and stack[-1] > item:
                ##若后边还有该字符
                if count[stack[-1]] == 0: break
                flag[stack.pop()] = False
            stack.append(item)
            flag[item] = True
        return "".join(stack)
