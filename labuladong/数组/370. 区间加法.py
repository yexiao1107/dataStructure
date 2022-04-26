'''
假设你有一个长度为 n 的数组，初始情况下所有的数字均为 0，你将会被给出 k​​​​​​​ 个更新的操作。

其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，你需要将子数组 A[startIndex ... endIndex]（包括 startIndex 和 endIndex）增加 inc。

请你返回 k 次操作后的数组。

示例:

输入: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
输出: [-2,0,3,5,3]
解释:

初始状态:
[0,0,0,0,0]

进行了操作 [1,3,2] 后的状态:
[0,2,2,2,0]

进行了操作 [2,4,3] 后的状态:
[0,2,5,5,3]

进行了操作 [0,2,-2] 后的状态:
[-2,0,3,5,3]
'''


class Diff():
    '''
    解题思路，差分数组，差分数据主要作为频繁修改数组元素的优化方法，可以利用该工具类解题
    '''

    def __init__(self, nums: [int]):
        '''
        构造差分数组
        '''
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len((nums))):
            self.diff[i] = nums[i] - nums[i - 1]

    def incer_num(self, i, j, num):
        self.diff[i] += num
        if (j + 1 < len(self.diff)): self.diff[j + 1] -= num

    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res


def nums_sum(length: int, updates: [[int]]):
    nums = [0] * length
    diff = Diff(nums)
    for update in updates:
        start, end, count = update[0], update[1], update[2]
        diff.incer_num(start, end, end)
    return diff.result()
