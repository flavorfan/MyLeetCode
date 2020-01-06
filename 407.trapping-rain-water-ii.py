#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#

# @lc code=start
from typing import List
from heapq import heappush, heappop
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not any(heightMap):
            return 0
        self.border = []
        self.visited = set()
        water = 0
        
        self.m, self.n = len(heightMap), len(heightMap[0])
        # 最小堆记录四个边的高度: 最小堆　＋　visited set
        for i in range(self.m):
            self.add(heightMap[i][0], i, 0)
            self.add(heightMap[i][self.n - 1], i, self.n - 1)
        for j in range(self.n):
            self.add(heightMap[0][j], 0, j)
            self.add(heightMap[self.m - 1][j], self.m - 1, j)
        
        # 最小堆确保一直从“当前木桶挡板最低处”漫延计算
        while self.border:
            height, x, y = heappop(self.border)
            for x, y in self.adjacent(x, y):
                water += max(0, height - heightMap[x][y])
                self.add(max(height, heightMap[x][y]), x, y)
        
        return water
            
    # 最小堆算法
    def add(self, height, x, y):
        heappush(self.border, (height, x, y))
        self.visited.add((x, y))
    
    # 计算相邻（visit）不重复
    def adjacent(self, x, y):
        adjacent = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_new = x + dx
            y_new = y + dy
            if 0 <= x_new < self.m and 0 <= y_new < self.n and (x_new, y_new) not in self.visited:
                adjacent.append((x_new, y_new))
        return adjacent
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    h = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] 
    print(sln.trapRainWater(h))