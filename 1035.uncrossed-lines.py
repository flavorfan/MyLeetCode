#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

# @lc code=start
from typing import List
class Solution:
    # Levenshtein distance with two matrix rows
    # 172ms 97%
    def maxUncrossedLines_1(self, A: List[int], B: List[int]) -> int:
        prev, crnt = [0] * (1 + len(B)), [0] * (1 + len(B))
        for a in range(len(A)):
            prev, crnt = crnt, prev
            for b in range(len(B)):
                if A[a] == B[b]:
                    crnt[b + 1] = prev[b] + 1
                else:
                    crnt[b + 1] = max(crnt[b], prev[b + 1])
        return crnt[len(B)]
    # 设 A[0] ~ A[x] 与 B[0] ~ B[y] 的最大连线数为 f(x, y)，那么对于任意位置的 f(i, j) 而言：
    # 如果 A[i] == B[j]，即 A[i] 和 B[j] 可连线，此时 f(i, j) = f(i - 1, j - 1) + 1
    # 如果 A[i] != B[j]，即 A[i] 和 B[j] 不可连线，此时最大连线数取决于 f(i - 1, j) 和 f(i, j - 1) 的较大值
    # 252ms 49.36% DP
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        a_length = len(A)
        b_length = len(B)
        
        res = [[0 for _ in range(b_length + 1)] for _ in range(a_length + 1)]
        
        for i in range(a_length):
            for j in range(b_length):
                if A[i] == B[j]:
                    res[i + 1][j + 1] = res[i][j] + 1
                else:
                    res[i + 1][j + 1] = max(res[i + 1][j], res[i][j + 1])
        
        return res[a_length][b_length]


# @lc code=end
if __name__ == '__main__':
    sln = Solution()
    A = [ 1, 4, 2 ]
    B = [ 1, 2, 4 ]
    print(sln.maxUncrossedLines(A,B))
