#
# @lc app=leetcode id=833 lang=python3
#
# [833] Find And Replace in String
#

# @lc code=start
# 32ms 84.88%
from typing import List
class Solution:
    def findReplaceString_1(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        # str to list[char]
        S = list(S)
        for i, x, y in sorted(zip(indexes, sources, targets), reverse = True):
            # all 实现满足全部迭代 all( yyy for xx in rr)
            if all(i+k < len(S) and S[i+k] == x[k] for k in range(len(x))):
                S[i:i+len(x)] = list(y)
        # list[char] to str
        return "".join(S)

    # map/dict (ind, src-target)
    # startwith to check
    # 36ms 61.11
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        lookup = {i: (src, tgt) for i, src, tgt in zip(indexes, sources, targets)}
        i, result = 0, ""
        while i < len(S):
            if i in lookup and S[i:].startswith(lookup[i][0]):
                result += lookup[i][1]
                i += len(lookup[i][0])
            else:
                result += S[i]
                i += 1
        return result

# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    S = "abcd"
    indexes = [0,2]
    sources = ["a","cd"]
    targets = ["eee","ffff"]
    print(sln.findReplaceString(S,indexes, sources,targets))