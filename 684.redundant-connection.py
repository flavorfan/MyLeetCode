#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
from typing import List
class UnionFind:
    def __init__(self, n):
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
            return False
        
        less, more = ((idp, idq) if self.size[idp] < self.size[idq] else (idq, idp))

        self.id[less] = self.id[more] 
        self.size[more] += self.size[less]
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(1001)
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge

        


if __name__ == "__main__":
    sln = Solution()
    es = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    print(sln.findRedundantConnection(es))
