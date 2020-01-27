#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
from typing import List
import collections 

class Solution:
    '''
    brute force with set
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        ans = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                x, y = A[i], A[i] + A[j]
                length = 2
                while y in s:
                    x, y = y, x + y
                    length += 1
                ans = max (ans, length)
        return ans if ans>=3 else 0
    '''
    ## dp: 672ms 72.09%
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = { x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0


# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    print(sln.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))