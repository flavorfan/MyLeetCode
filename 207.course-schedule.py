#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [ 0  for _ in range (numCourses)]
        adjacency = [ [] for _ in range (numCourses)]
        queue = []
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
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)
        
        return not numCourses

if __name__ == '__main__':
    sln = Solution()
    print(sln.canFinish(2,[[1,0]]))
    pass
# @lc code=end

