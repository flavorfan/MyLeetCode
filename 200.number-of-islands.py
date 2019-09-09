#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List
import operator
class UnionFind(object):
    def __init__(self,grid):
        self.m = len(grid)
        self.n = len(grid[0])
        self.length = self.m * self.n

        self.id = [None] * self.length
        self.size = [1] * self.length 
        self.surrounded = [True] * self.length

        ## 
        [operator.setitem(self.id, *([self.getIndex(i,j)] * 2))
        for i,row in enumerate(grid)
        for j,val in enumerate(row) if val == '1']

    def getIndex(self,i,j):
        return self.n * i + j
    
    def find(self,p):
        while p != self.id[p]:
            self.id[p] =self.id[self.id[p]]
            p = self.id[p]
        return p
    
    def union(self, p, q):
        idp, idq = map(self.find, (p,q))
        if idp == idq:
            return 

        less, more = (
            (idp, idq) if self.size[idp] < self.size[idq] else (idq, idp))
        
        self.id[less] = self.id[more]
        self.size[more] += self.size[less]
        self.surrounded[more] = self.surrounded[less] and self.surrounded[more]



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        uf = UnionFind(grid)

        for i,row in enumerate(grid):
            for j, val in enumerate(row):
                if val != '1':
                    continue
                index = uf.getIndex(i,j)
                [uf.union(index, uf.getIndex(y,z))
                    for x, y, z in ((i,i-1, j), (j, i, j-1))
                    if x > 0 and grid[y][z] == '1'
                ]
        return len(set([ uf.find(uf.getIndex(i,j)) 
                for i,row in enumerate(grid)
                for j,val in enumerate(row) if val == '1']))

        

if __name__ == "__main__":
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"],
            ["0","0","0","1","1"]]
    sln = Solution()
    print(sln.numIslands(grid))
    pass
