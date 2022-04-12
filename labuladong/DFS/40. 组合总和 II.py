'''
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。 

 

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
'''


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtrack(candidates, start, target):
            if self.sums == target:
                res.append(track[:])
                return
            if self.sums > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]: continue
                self.sums += candidates[i]
                track.append(candidates[i])
                backtrack(candidates, i + 1, target)
                self.sums -= candidates[i]
                track.pop()

        candidates = sorted(candidates)
        self.sums = 0
        res = []
        track = []
        backtrack(candidates, 0, target)
        return res