#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#

# @lc code=start
from typing import List
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return abs(nums[0] - 24) < 10**-3
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                add = nums[i] + nums[j]
                minus = nums[i] - nums[j]
                time = nums[i] * nums[j]
                
                nl = nums[:i] + nums[i + 1:j] + nums[j + 1:]
                res = self.judgePoint24(nl + [add]) or self.judgePoint24(nl + [minus]) or self.judgePoint24(nl + [time]) or self.judgePoint24(nl + [-minus])
                if nums[j] != 0 and nums[i] != 0:
                    divide = nums[i] / nums[j]
                    res = res or self.judgePoint24(nl + [divide]) or self.judgePoint24(nl + [1/divide])
                if res:
                    return True
        return False        
        
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    print(sln.judgePoint24([4, 1, 8, 7]))

