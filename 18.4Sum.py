"""
Given an array nums of n integers and an integer target, are there elements a, b, c,
 and d in nums such that a + b + c + d = target?

 Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
import bisect

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = self.NSum(nums,target,4)
        ans = list(set([tuple(t) for t in ans]))
        ans = [list(v) for v in ans ]
        return ans

    # res = list(set([tuple(t) for t in res]))
    # res = [list(v) for v in res]

    def NSum(self, nums, target,cnt ):
        """
        :type nums: sorted List[int]
        :type target: int
        :type cnt: int  nSum >=2
        :rtype: List[List[int]]
        """
        N = len(nums)
        ans = []
        if cnt == 2:
            left = 0
            right = N - 1
            while left < right:
                cur = nums[left] + nums[right]
                if  cur < target:
                    left += 1
                elif cur > target:
                    right -= 1
                else:
                    ans.append([nums[left],nums[right]])
                    left += 1
        else:
            for i in range(N -cnt+1):
                next_tar = target- nums[i]
                next_ans = self.NSum(nums[i+1:],next_tar,cnt-1)
                for j in next_ans:
                    j.append(nums[i])
                    ans.append(j)

        return ans

    def fourSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        w = sorted(nums)
        res = []
        for i in range(len(w) - 3):
            for j in range(i + 1, len(w) - 2):
                start = j + 1
                end = len(w) - 1
                while start < end:
                    value = w[i] + w[j] + w[start] + w[end]
                    if value == target:
                        res.append([w[i], w[j], w[start], w[end]])
                        start += 1
                    elif value < target:
                        start += 1
                    elif value > target:
                        end -= 1
        res = list(set([tuple(t) for t in res]))
        res = [list(v) for v in res]
        return res

    def fourSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        pair_mp = []
        



if __name__ == '__main__':
    # nums = [1, 0, -1, 0, -2, 2]
    # nums = [0,0,0,0]
    nums = [-3,-2,-1,0,0,1,2,3]

    target = 0
    sln = Solution()
    print(sln.fourSum(nums,target))
