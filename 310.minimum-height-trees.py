#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
from typing import List
import collections
class Solution:
    def findMinHeightTrees_2(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        graph = collections.defaultdict(list)
        degree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        queue = [ n for n in range(n) if degree[n]==1 ]
        # 每次去除一层叶子节点，这样保证最后的节点就是我们所要的。
        while queue:
            tmp = []
            ans = queue
            for leaf in queue:
                for nei in graph[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        tmp.append(nei)
            queue = tmp
        return ans
    # High level idea is to keep pruning the outer node which has zero or one edge from the tree.
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = [set() for _ in range(n)]
        for u, v in edges: tree[u].add(v), tree[v].add(u)
        q, nq = [x for x in range(n) if len(tree[x]) < 2], []
        while True:
            for x in q:
                for y in tree[x]:
                    tree[y].remove(x)
                    if len(tree[y]) == 1: nq.append(y)
            if not nq: break
            nq, q = [], nq
        return q
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    n = 4
    edges =  [[1, 0], [1, 2], [1, 3]]
    print(sln.findMinHeightTrees(n,edges))

