#
# @lc app=leetcode id=675 lang=python3
#
# [675] Cut Off Trees for Golf Event
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:             
        # 对于位置 (r, c) 的每个节点，我们使 node.f = node.g + node.h
        # node.g 是从 (sr, sc) 到 (r, c) 的实际距离， 
        # node.h 是从 (r, c) 到 (tr, tc) 的距离的启发式（猜测）   
        # 在这种情况下，我们的猜测将是  node.h = abs(r-tr) + abs(c-tc)
        # 熟悉 Dijkstra 算法的人来说，知道一个 A*搜索是 Dijkstra 的一个特例，且 node.h 总是 0。
        def astar(forest, passable, ibeg, jbeg, iend, jend):
            h, w = len(forest), len(forest[0])
            
            seen = {(ibeg, jbeg)}
            # weight(f) , traved(g), ibeg(r),jbeg(c)
            heap = [(0, 0, ibeg, jbeg)]
                        
            while heap:
                _, traveled, i, j = heapq.heappop(heap)
                if i == iend and j == jend:
                    return traveled

                for cords in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if cords not in seen and cords in passable:
                        ni, nj = cords
                        seen.add(cords)
                        weight = traveled + 1 + abs(ni - iend) + abs(nj - jend)
                        heapq.heappush(heap, (weight, traveled + 1, ni, nj))
            return -1

        # 计算可行路线，和需要砍的树　　：　passable  trees
        passable = set()
        trees = []
        for i, row in enumerate(forest):
            for j, val in enumerate(row):
                if val > 0:
                    passable.add((i, j))
                    if val > 1:
                        trees.append((val, i, j))

        path = 0
        ibeg, jbeg = 0, 0
        for _, iend, jend in sorted(trees):
            segmentPath = astar(forest, passable, ibeg, jbeg, iend, jend)
            if segmentPath < 0:
                return -1
            
            path += segmentPath
            ibeg, jbeg = iend, jend
            
        return path
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    forest = [[1,2,3],[0,0,4],[7,6,5]]
    print(sln.cutOffTree(forest))