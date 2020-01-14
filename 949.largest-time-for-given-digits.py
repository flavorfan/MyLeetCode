#
# @lc app=leetcode id=949 lang=python3
#
# [949] Largest Time for Given Digits
#

# @lc code=start
from typing import List
import itertools
# 28ms 80.83
# 高效循环的　itertools.permutations
# 排列组合迭代器：长度r元组，所有可能的排列，无重复元素

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""
# @lc code=end

if __name__ == "__main__":
    sln = Solution()
    A = [1,2,3,4]
    print(sln.largestTimeFromDigits(A)) # "23:41"