#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#
from typing import List
# @lc code=start
class Solution:
    def findSubsequences_dfs(self, nums: List[int]) -> List[List[int]]:
        result = []
        sofar = []

        def dfs(i):
            if len(sofar) >= 2:
                result.append(list(sofar))
            seen = set()
            prev = sofar[-1] if sofar else float('-inf')
            for j in range(i, len(nums)):
                if (nums[j] >= prev and nums[j] not in seen):
                    seen.add(nums[j])
                    sofar.append(nums[j])
                    dfs(j+1)
                    sofar.pop()
            
        dfs(0)
        return result
    # A conceptually easier solution is use tuple to represent each sequence 
    # (so that it's hashable), and use a set to hold all sequences,
    #  which automatically takes care of duplicates.
    def findSubsequences_tuple(self, nums: List[int]) -> List[List[int]]:
        res = {()}
        for n in nums:
            res |= {tup+(n,) for tup in res if not tup or tup[-1] <= n}
        return [list(x) for x in res if len(x) >= 2]
    
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        num2idx = {}
        idx2res = {}
        for i in range(len(nums)):
            if nums[i] not in num2idx:
                start = 0
                idx2res[i] = [[nums[i]]]
            else:
                start = num2idx[nums[i]]
                idx2res[i] = []
            for j in range(start, i):
                if nums[j] <= nums[i]:
                    for seq in idx2res[j]:
                        tmp = list(seq)
                        tmp.append(nums[i])
                        idx2res[i].append(tmp)
                        res.append(tmp)
            num2idx[nums[i]] = i
        return res
        
# @lc code=end
if __name__ == '__main__':
    sln = Solution()
    input = [4, 6, 7, 7]
    print(sln.findSubsequences(input))
 