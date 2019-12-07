#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from typing import List
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        if rows == 0:
            return[]
        cols = len(matrix[0])
        mx = rows * cols 
        dis = [[mx for _ in range(cols)] for _ in range(rows)]

        print(dis)    
        for i in range(rows-1, -1, -1):
            for j in range(cols -1, -1, -1):
                if matrix[i][j] == 0:
                    dis[i][j] = 0
                else:
                    right = dis[i][j+1] if j+1 < cols else mx 
                    down  = dis[i+1][j] if i+1 < rows else mx
                    dis[i][j] = 1 + min(right, down)
        print(dis)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dis[i][j] = 0
                else:
                    left  = dis[i][j-1] if j-1 >= 0   else mx 
                    top   = dis[i-1][j] if i-1 >= 0   else mx
                    dis[i][j] = min( dis[i][j], 1 + min(left, top))
        
        return dis

        
        
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    matrix =[[0,0,0],[0,1,0],[1,1,1]]
    print(sln.updateMatrix(matrix))

