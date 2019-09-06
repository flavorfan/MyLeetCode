#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#
#  first identify the node with two parents, then identify the cycle edg
# 1 [two parents] [no cycle]: pick the edge occurs last in the given edges.
#   1   
#  / \
# v   v
# 2-->3
# 2 [two parents] [cycle]:  node 4 two parents and consists of the cycle.
# 5 -> 1 -> 2
#      ^    |
#      |    v
#      4 <- 3

# 3 [cycle] : dge occurs last in the given edges
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3

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
    def union(self, p, q): # i p
        idp, idq = self.find(p), self.find(q)
        if idp == idq:
            return False
        
        # less, more = ((idp, idq) if self.size[idp] < self.size[idq] else (idq, idp))

        # self.id[less] = self.id[more] 
        # self.size[more] += self.size[less]
        self.id[idq] = self.id[idp]  # child -> parent
        return True

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n, p1, p2, c = len(edges), None, None, None
        p = [0] * (n+1)

        for i, (u,v) in enumerate(edges):
            if p[v]: 
                # If there is a node with two parent, p1->c, p2->c. 
                # delete the later one p2->c and then check if there is a cycle.
                p1, p2, c, edges[i][0] = p[v], u, v, 0
            else: 
                p[v] = u
        p = list(range(n+1))

        # find
        def find(x):
            if p[x] != x: p[x] = find(p[x])
            return p[x]

        for u, v in edges:
            if u:
                pu, pv = find(u), find(v)
            if pu == pv: return p1 and [p1, c] or [u, v]
            else: p[pv] = pu
        return [p2, c]
        

if __name__ == "__main__":
    sln = Solution()
    es = [[1,2], [1,3], [2,3]]
    print(sln.findRedundantDirectedConnection(es))
