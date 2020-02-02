#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        height = len(matrix)
        if height == 0 or len(matrix[0]) == 0:
            return 0
        width = len(matrix[0])
        d = [[None] * width for _ in range(height)]
        m = min([min(v) for v in matrix])
        
        def dfs(r, c):
            if d[r][c] is None:
                d[r][c] = 1
                if matrix[r][c] != m:
                    if r > 0 and matrix[r - 1][c] < matrix[r][c]:
                        d[r][c] = max(d[r][c], dfs(r - 1, c) + 1)
                    if r < height - 1 and matrix[r + 1][c] < matrix[r][c]:
                        d[r][c] = max(d[r][c], dfs(r + 1, c) + 1)
                    if c > 0 and matrix[r][c - 1] < matrix[r][c]:
                        d[r][c] = max(d[r][c], dfs(r, c - 1) + 1)
                    if c < width - 1 and matrix[r][c + 1] < matrix[r][c]:
                        d[r][c] = max(d[r][c], dfs(r, c + 1) + 1)
            return d[r][c]
        for y in range(height):
            for x in range(width):
                dfs(y, x)
        return max([max(v) for v in d])
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    nums = [
            [9,9,4],
            [6,6,8],
            [2,1,1]
        ] 
    
    print(sln.longestIncreasingPath(nums))