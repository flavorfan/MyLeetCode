#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# @lc code=start
from typing import List
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])
        memo = [[0] * C for _ in range(R)] # 0:not visited  1:pacific  2:atlantic  3:both
        ans = []

        def df(r, c,POrA):
            memoV = memo[r][c]
            if memoV==POrA or memoV==3:
                return
            if memoV==0:
                memo[r][c] = POrA
            else: #memoV==1 if POrA==2. memoV==2 if POrA==1
                memo[r][c] = 3
                ans.append([r, c])            
            for rd, cd in ((1,0),(-1,0),(0,1),(0,-1)):
                r2, c2 = r+rd, c+cd
                if 0<=r2<R and 0<=c2<C and matrix[r2][c2]>=matrix[r][c]:
                    df(r2, c2, POrA)

        for r in range(R):
            df(r, 0, 1)
            df(r, C-1, 2)
        for c in range(C):
            df(0, c, 1)
            df(R-1, c, 2)
        return ans
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(sln.pacificAtlantic(matrix))
