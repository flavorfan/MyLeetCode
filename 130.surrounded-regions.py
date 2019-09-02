#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# X X X X
# X O O X
# X X O X
# X O X X

# X X X X
# X X X X
# X X X X
# X O X X

from typing import List
import operator

class UnionFind(object):
    def __init__(self,board):
        self.m = len(board)
        self.n = len(board[0])
        self.length = self.m * self.n

        self.id = [None] * self.length
        self.size = [1] * self.length 
        self.surrounded = [True] * self.length

        ## 
        [operator.setitem(self.id, *([self.getIndex(i,j)] * 2))
        for i,row in enumerate(board)
        for j,val in enumerate(row) if val == 'O']

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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        uf = UnionFind(board)

        for i,row in enumerate(board):
            for j, val in enumerate(row):
                if val != 'O':
                    continue
                
                index = uf.getIndex(i, j)

                [uf.union(index, uf.getIndex(y, z))
                    for x, y , z in ((i, i-1, j), (j, i, j-1))
                    if x > 0 and board[y][z] == 'O']

                if i == 0 or j == 0 or i == uf.m - 1 or j == uf.n - 1:
                    uf.surrounded[uf.find(index)] = False
        
        [operator.setitem(board[i], j, 'X')
         for i in range(uf.m)
         for j in range(uf.n)
         if board[i][j] == 'O' and uf.surrounded[uf.find(uf.getIndex(i, j))]]

        
if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sln = Solution()
    sln.solve(board)
    print(board)
    pass
