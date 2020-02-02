#
# @lc app=leetcode id=514 lang=python3
#
# [514] Freedom Trail
#
# 动态规划：　ｄｐ保留当前的选择的可能，ｎｅｗ——ｄｐ在后续扩展新的可能性
# @lc code=start
from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        N, M = len(ring), len(key)
        
        idxs = defaultdict(list)
        for i, c in enumerate(ring):
            idxs[c].append(i)
        
        dp = [(0, M)]
        for i in range(M):
            newdp = []
            for nxti in idxs[key[i]]:
                tmp = None
                for prei, val in dp:
                    nxtv = min(abs(nxti - prei), N-abs(nxti - prei)) + val
                    if tmp is None or tmp > nxtv:
                        tmp = nxtv
                newdp.append((nxti, tmp))
            dp = newdp
        return min([t[1] for t in dp])
        
# @lc code=end
if __name__ == '__main__':
    sln = Solution()
    print(sln.findRotateSteps("godding","gd"))
