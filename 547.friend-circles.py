#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#
from typing import List
class UnionFind:
    def __init__(self,n):
        self.id = [i for i in range(n)]
        self.size =[1] * n
    def find(self,p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p
    def union(self, p, q):
        idp, idq = self.find(p), self.find(q)
        if idp == idq:
            return
        
        less, more = ((idp, idq) if self.size[idp] < self.size[idq] else (idq, idp))

        self.id[less] = self.id[more] 
        self.size[more] += self.size[less]

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M : 
            return 0
        length = len(M)
        uf = UnionFind(length)

        for r in range(length):
            for c in range(length):
                if M[r][c] == 1: 
                    uf.union(r,c)
        
        return len(set([uf.find(i) for i in range(length)]))

        
if __name__ == '__main__':
    sln = Solution()
    m = [[1,1,0],[1,1,0],[0,0,1]]
    m2 = [[1,1,0],[1,1,1],[0,1,1]]
    print(sln.findCircleNum(m))
    print(sln.findCircleNum(m2))

