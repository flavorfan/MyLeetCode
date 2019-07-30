"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
import sys
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums) -1
        dp= [sys.maxsize] * N

        if  N <= 0 :
            return 0
        for i in range(N-1,-1,-1):
            cur = nums[i]
            if cur == 0:
                continue
            if cur + i < N:
                for j in range(cur, 0, -1):
                    if dp[i + j] != sys.maxsize:
                        dp[i] = min(dp[i], dp[i + j] + 1)
            else:
                dp[i] = 1

        return dp[0]
    
    def jump2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        end = next_end = 0
        for i in range(len(nums)-1):
            next_end = max(next_end, i+nums[i])
            if i == end:
                ans += 1
                end, next_end = next_end, next_end + 1
        return ans

if __name__ == '__main__':
    # nums = [2,3,1,1,4]  # out put 2
    nums = [1,3,7,0,0,0,10,0,0,3,0,0,0,0,4]  # out put 2
    sln = Solution()
    print(sln.jump2(nums))


