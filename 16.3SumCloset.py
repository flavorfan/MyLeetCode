"""
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = sum(nums[:3])
        N = len(nums)

        min_dis = float('inf')

        for i in range(N-2):
            left = i +1;
            right = N-1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                dis = cur_sum - target;
                if  abs(dis) < min_dis:
                    min_dis = abs(dis)
                    ans = cur_sum
                if dis < 0:
                    left += 1
                elif dis > 0:
                    right -=1
                else:
                    return ans
        return ans

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    sln = Solution()
    print(sln.threeSumClosest(nums,target))