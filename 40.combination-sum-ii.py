#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

from typing import List

class Solution:
    def __dfs(self,candidates, start, path,  residuce):
        if residuce == 0:
            self.ans.append(path[:])
            return       
        for idx in range(start,len(candidates)):
            if candidates[idx] > residuce:
                break       
            if idx > start and candidates[idx - 1] == candidates[idx]:
                continue             
            path.append(candidates[idx])
            self.__dfs(candidates,idx + 1, path, residuce - candidates[idx])
            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        candidates.sort()
        self.ans = []
        self.__dfs(candidates,0,[],target)
        return self.ans
        

if __name__ == '__main__' :
    candidates = [10,1,2,7,6,1,5]
    target = 8
    sln = Solution()
    print(sln.combinationSum2(candidates,target))