'''
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。

 

示例 1：

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
示例 2：

输入：s1= "ab" s2 = "eidboaoo"
输出：false
 

提示：

1 <= s1.length, s2.length <= 104
s1 和 s2 仅包含小写字母
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        need, window = {}, {}
        for c in s1: need[c] = need.get(c, 0) + 1
        vaild = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if need[c] == window[c]:
                    vaild += 1
            while right - left >= len(s1):
                d = s2[left]
                left += 1
                if vaild == len(need):
                    return True
                if d in need:
                    if need[d] == window[d]:
                        vaild -= 1
                    window[d] = window[d] - 1
        return False
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkInclusion("abcdxabcde", "abcdeabcdx"))
