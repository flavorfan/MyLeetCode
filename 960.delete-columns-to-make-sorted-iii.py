#
# @lc app=leetcode id=960 lang=python3
#
# [960] Delete Columns to Make Sorted III
#
# try to find the number of columns to keep, instead of the number to delete.
# Let dp[k] be the number of columns that are kept in answering the question 
# for input [row[k:] for row in A]. The above gives a simple recursion for dp[k].
from typing import List
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        W = len(A[0])
        dp = [1] * W
        for i in range(W-2,-1,-1):
            for j in range(i+1, W):
                if all(row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], 1+ dp[j])
        return W - max(dp)
        


if __name__ == "__main__":
    sln = Solution()
    A = ["babca","bbazb"]
    print(sln.minDeletionSize(A))

