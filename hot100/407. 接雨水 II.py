'''
给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。

 

示例 1:



输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
输出: 4
解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
示例 2:



输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
输出: 10
'''


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        import heapq
        m, n, ans = len(heightMap), len(heightMap[0]), 0
        visited, dirs, pq = [[False] * n for _ in range(m)], [(0, 1), (1, 0), (0, -1), (-1, 0)], []
        for i in range(1, n - 1):
            heapq.heappush(pq, (heightMap[0][i], 0, i))
            heapq.heappush(pq, (heightMap[m - 1][i], m - 1, i))
        for i in range(1, m - 1):
            heapq.heappush(pq, (heightMap[i][0], i, 0))
            heapq.heappush(pq, (heightMap[i][n - 1], i, n - 1))
        while pq:
            h, x, y = heapq.heappop(pq)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 < nx < m - 1 and 0 < ny < n - 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    ans += max(0, h - heightMap[nx][ny])
                    heapq.heappush(pq, (max(h, heightMap[nx][ny]), nx, ny))
        return ans


if __name__ == "__main__":
    import heapq

    queue = []
    heapq.heappush(queue, (0, 1, 2))
    print(heapq.heappop(queue))
