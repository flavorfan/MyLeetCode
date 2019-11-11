#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjMap = self.makeAdjMap(tickets)
        res = []
        self.dfs(adjMap, "JFK", res)
        return res[::-1]
    
    def dfs(self, adjMap, airport, res):
        if airport in adjMap and len(adjMap[airport]) > 0:        
            while len(adjMap[airport]) > 0:
                destination = adjMap[airport].pop()
                self.dfs(adjMap, destination, res)
        res.append(airport)
    
    # 构建临近表，深度遍历用来保存所有可能性
    def makeAdjMap(self, tickets):
        adjMap = {}
        for ticket in tickets:
            if ticket[0] not in adjMap:
                adjMap[ticket[0]] = [ticket[1]]
            else:
                adjMap[ticket[0]].append(ticket[1])
        for ticket in tickets:
            adjMap[ticket[0]].sort(reverse=True)
        return adjMap    
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    input = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print(sln.findItinerary(input))
