'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true
 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def getVaule(item):
            if item == ")":
                return "("
            elif item == "]":
                return "["
            elif item == "}":
                return "{"

        stack = []
        for item in s:
            if item == "(" or item == "[" or item == "{":
                stack.append(item)
            else:
                if stack and stack[-1] == getVaule(item):
                    stack.pop()
                else:
                    return False
        return True if not stack else False

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("{[()]}"))
