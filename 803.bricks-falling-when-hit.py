#
# @lc app=leetcode id=803 lang=python3
#
# [803] Bricks Falling When Hit
#

# @lc code=start

# 1: Reverse Time and Union-Find 
# 倒过来考虑这个过程：每次我们加上一个砖块，
# 并计算有多少额外的砖块因为这个砖块的增加而和网格的顶部直接或间接相连。
# 这样我们就可以用并查集来解决这个问题了。

# 添加一个虚拟的节点，它的编号为 R * C（网格中的节点编号为 [0, R * C - 1]），
# 代表网格的顶部，任何第一行的砖块都会与它相连。
# 对于网格中的每一个位置，如果它在所有操作结束后仍然有砖块，
# 那么就将它和四连通（上下左右）的四个位置（如果对应位置也有砖块）进行合并。
# 这样，我们就得到了在所有操作结束后，网格对应的并查集状态。


from typing import List
# 960ms 24.53%
class DSU:
    def __init__(self, R, C):
        #R * C is the source, and isn't a grid square
        self.par = list(range(R*C + 1))
        self.rnk = [0] * (R*C + 1)
        self.sz = [1] * (R*C + 1)

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1

        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]

    def size(self, x):
        return self.sz[self.find(x)]

    def top(self):
        # Size of component at ephemeral "source" node at index R*C,
        # minus 1 to not count the source itself in the size
        return self.size(len(self.sz) - 1) - 1


class Solution_1:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        def index(r, c): 
            return r * C + c

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        # List[List] to ararry[][]
        A = [row[:] for row in grid]
        for i, j in hits:
            A[i][j] = 0

        # use union find unit to creat union
        dsu = DSU(R, C)
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val:
                    i = index(r, c)
                    if r == 0:
                        dsu.union(i, R*C)
                    if r and A[r-1][c]:
                        dsu.union(i, index(r-1, c))
                    if c and A[r][c-1]:
                        dsu.union(i, index(r, c-1))

        # reversed hit
        ans = []
        for r, c in reversed(hits):
            pre_roof = dsu.top()
            # not hit any thing
            if grid[r][c] == 0:
                ans.append(0)
            else:
                i = index(r, c)
                for nr, nc in neighbors(r, c):
                    if A[nr][nc]:
                        dsu.union(i, index(nr, nc))
                if r == 0:
                    dsu.union(i, R*C)
                A[r][c] = 1
                ans.append(max(0, dsu.top() - pre_roof - 1))
        return ans[::-1]
        
# 2560ms 5.66%
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        inf = float('inf')
        for (i, j) in hits:
            if grid[i][j] == 1:
                grid[i][j] = -1
        
        def nbrs(i, j):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ci, cj = i + di, j + dj
                if ci < 0 or ci >= m or cj < 0 or cj >= n: continue
                yield ci, cj
        
        def stick(i, j):
            grid[i][j] = inf
            for ni, nj in nbrs(i, j):
                if grid[ni][nj] == 1:
                    stick(ni, nj)
        
        for j in range(n):
            if grid[0][j] == 1: stick(0, j)
        ans = []
        def put_back(i, j, visited):
            grid[i][j] = inf if i == 0 or any(grid[ni][nj] == inf for ni, nj in nbrs(i, j)) else 1
            ans = 1 if grid[i][j] == inf else 0
            for ni, nj in nbrs(i, j):
                if grid[ni][nj] != 1 or (ni, nj) in visited: continue
                visited.add((ni, nj))
                ans += put_back(ni, nj, visited)
            return ans
        for (i, j) in hits[::-1]:
            ans.append(put_back(i, j, set([(i, j)]))-(grid[i][j] == inf) if grid[i][j] == -1 else 0)
        return ans[::-1]

        
# @lc code=end
if __name__ == '__main__':
    sln = Solution()
    grid = [[1,0,0,0],[1,1,1,0]]
    hits = [[1,0]]
    print(sln.hitBricks(grid,hits))

