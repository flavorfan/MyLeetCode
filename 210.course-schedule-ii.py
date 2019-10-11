#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [ 0  for _ in range (numCourses)]
        adjacency = [ [] for _ in range (numCourses)]
        queue = []
        ans = []
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS Topsort
        while queue:
            pre = queue.pop(0)
            ans.append(pre)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)
        
        if not numCourses: 
            return ans 
        else:
            return []

if __name__ == '__main__':
    sln = Solution()
    print(sln.findOrder(2,[[1,0]]))
# @lc code=end

