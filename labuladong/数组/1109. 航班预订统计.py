'''
这里有 n 个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。

 

示例 1：

输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]
解释：
航班编号        1   2   3   4   5
预订记录 1 ：   10  10
预订记录 2 ：       20  20
预订记录 3 ：       25  25  25  25
总座位数：      10  55  45  25  25
因此，answer = [10,55,45,25,25]
示例 2：

输入：bookings = [[1,2,10],[2,2,15]], n = 2
输出：[10,25]
解释：
航班编号        1   2
预订记录 1 ：   10  10
预订记录 2 ：       15
总座位数：      10  25
因此，answer = [10,25]
 

提示：

1 <= n <= 2 * 104
1 <= bookings.length <= 2 * 104
bookings[i].length == 3
1 <= firsti <= lasti <= n
1 <= seatsi <= 104
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


class Solution:
    def corpFlightBookings(self, bookings: [[int]], n: int) -> [int]:
        '''
        差分数组解法，i,j减1即可
        '''
        res = [0] * n
        diff = Diff(res)
        for booking in bookings:
            start, end, num = booking[0] - 1, booking[1] - 1, booking[2]
            diff.incer_num(start, end, num)
        return diff.result()