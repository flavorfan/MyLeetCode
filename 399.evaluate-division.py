#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
from typing import List
# class UnionFind:
#     def __init__(self,n):
#         self.id = [i for i in range(n)]
#         self.size =[1] * n
#     def find(self,p):
#         while p != self.id[p]:
#             self.id[p] = self.id[self.id[p]]
#             p = self.id[p]
#         return p
#     def union(self, p, q):
#         idp, idq = self.find(p), self.find(q)
#         if idp == idq:
#             return
        
#         less, more = ((idp, idq) if self.size[idp] < self.size[idq] else (idq, idp))

#         self.id[less] = self.id[more] 
#         self.size[more] += self.size[less]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        root = {}
        # xp = x/parent(x), pr = parent(x)/root(x), update xr to xr*pr = x/root(x)
        def find(x):
            p, xp = root.setdefault(x,(x, 1.0))
            if x != p: 
                r, pr = find(p)
                root[x] = (r, xp * pr)
            return root[x]
        
        # if root(x) = root(y), equations "x / y" doable as (x/root(x)) / (y/root(y)) = xr / yr
        def union(x, y, load):
            px, xr, py, yr = * find(x), * find(y)
            if not load:
                return xr / yr if px == py else -1.0
            if px != py: 
                root[px] = (py, yr / xr * load)
        
        for (x,y), v in zip(equations, values):
            union(x,y,v)
        return [ union(x,y,0) if x in root and y in root else -1.0 for x,y in queries]

if __name__ == "__main__":
    equations = [ ["a", "b"], ["b", "c"] ]
    values = [2.0, 3.0]
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
    sln = Solution()
    print(sln.calcEquation(equations,values,queries))

