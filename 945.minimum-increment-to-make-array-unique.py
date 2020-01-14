#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start
from typing import List
import collections
class Solution:
    # 时间太长，一次加１太慢
    def minIncrementForUnique_1(self, A: List[int]) -> int:
        ans = 0
        A.sort()
        for i in range(1,len(A)):
            while A[i] <= A[i-1]:
                A[i] += 1
                ans += 1
        return ans

    ## 如果 x 出现了两次以上，就将额外出现的数记录下来（例如保存到一个列表中）；
    ## 如果 x 没有出现过，那么在记录下来的数中选取一个 v，将它增加到 x，需要进行的操作次数为 x - v。
    # 1300ms 11.4%
    def minIncrementForUnique_2(self, A: List[int]) -> int:
        count = collections.Counter(A)
        taken = []

        ans = 0
        for x in range(100000):
            if count[x] >= 2:
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                ans += x - taken.pop()
        return ans

    # 如果 A[i - 1] == A[i]，我们将操作次数减去 A[i]，并将重复的数的个数增加 1；
    # 如果 A[i - 1] < A[i]，我们就可以将之前重复的数放入区间 (A[i - 1], A[i]) 中。
    # 设当前重复的数的个数为 taken，我们可以放入 give = min(taken, A[i] - A[i - 1] - 1) 个数，它们的和为
    # 352ms 64.69%
    def minIncrementForUnique(self, A):
        A.sort()
        A.append(100000)
        ans = taken = 0

        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                taken += 1
                ans -= A[i]
            # taken 多少个相同的
            else:
                give = min(taken, A[i] - A[i-1] - 1)
                ans += give * (give + 1) // 2 + give * A[i-1]
                taken -= give

        return ans


    
# @lc code=end
if __name__ == '__main__':
    sln = Solution()
    A = [3,2,1,2,1,7]
    print(sln.minIncrementForUnique(A))
