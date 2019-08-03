#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List
class Solution:
    def backtrack(self,candidates: List[int], target: int, chosen: List[int], total: int, start: int) :
        if total >= target :
            if total == target :
                self.ans.append(chosen)
            return -1
        for i in range(start, len(candidates)) :
            e = self.backtrack(candidates,target,chosen + [candidates[i]],total + candidates[i], i)
            if e == -1 :
                break

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not len(candidates) or target == 0:
            return []
        
        candidates.sort()
        self.ans = []
        self.backtrack(candidates,target,[],0,0)
        return self.ans



if __name__ == '__main__' :
    candidates = [2,3,6,7]
    target = 7
    sln = Solution()
    print(sln.combinationSum(candidates,target))