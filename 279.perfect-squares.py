#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        if n == 0 or n == 1: return n
        if int(n ** 0.5) ** 2 == n: return 1
        queue = deque([n])
        candidates = set([i ** 2 for i in range(1, int(n ** 0.5) + 1)])
        step = 0
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                tmp = queue.pop()
                for x in candidates:
                    val = tmp - x
                    if val in candidates:
                        return step + 1
                    elif val > 0:
                        queue.appendleft(val)

# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    print(sln.numSquares(13))