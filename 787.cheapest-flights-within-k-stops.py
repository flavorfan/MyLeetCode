#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
from typing import List
from collections import defaultdict
import heapq

# bfs 80ms 89.11%
class Solution_bfs:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0
        if not flights:
            return -1
        
        graph = defaultdict(list)
        for s, d, p in flights:
            graph[s].append((p, d))
        
        res = {src:0}
        self.BFS(graph, src, K, res)
        
        if dst in res:
            return res[dst]
        return -1
    
    def BFS(self, graph, src, K, res):
        frontier = [src]
        while frontier and K >= 0:
            nxt = []
            nxt_cost = []
            for cur in frontier:
                cur_cost = res[cur]
                for p, d in graph[cur]:
                    nxt_cost.append((p+cur_cost, d))
            for p, d in nxt_cost:
                if d not in res or p < res[d]:
                    res[d] = p
                    nxt.append(d)
            frontier = nxt
            K -= 1
        return

# Dijkstra's algorithm
# maintain a cost heap, pop out the cheapest flight and push in new flight entries to next destination.
# Build graph time: O(E), space: O(n)
# max heapq size is n with each node got pushed and popped once, time: O(nlogn), space: O(n)
# Overall: time O(E+nlogn) space O(n)

# 92ms 63.78%
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0
        if not flights:
            return -1

        flights_graph = defaultdict(list)
        for s, d, p in flights:
            flights_graph[s].append((d,p))

        # Assume arrival is also a stop
        max_stop = K + 1
        # heap item is (price, dst, stops)
        # At src, the cost to src is 0 and has 0 stops
        cost_heap = [(0,src,0)]
        while cost_heap:
            cur_p, cur, stop = heapq.heappop(cost_heap)
            if stop > max_stop:
                continue
            if cur == dst:
                return cur_p
            for nxt, nxt_p in flights_graph[cur]:
                heapq.heappush(cost_heap, (cur_p+nxt_p, nxt, stop+1))
        return -1
# @lc code=end

if __name__ == '__main__':
    n = 3
    edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    sln = Solution()
    print(sln.findCheapestPrice(n, edges, src, dst, k))
