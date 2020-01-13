#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
from typing import List
import collections

class Solution:
    # use counter
    # 28ms 64.93
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        # ans = []
        counter = collections.Counter(A.split() + B.split())
        # for k, v in counter.items():
        #     # print(k, v)
        #     if v == 1:
        #         ans.append(k)
        # return ans 
        return [word for word in counter if counter[word] == 1]
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    A = "this apple is sweet"
    B = "this apple is sour"
    print(sln.uncommonFromSentences(A,B))

