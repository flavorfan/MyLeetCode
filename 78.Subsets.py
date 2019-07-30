"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

P({∅}) = [[∅]]
P({1}) = [[∅], [1]]
P({1, 2}) = [[∅], [1], [2], [1, 2]]
P({1, 2, 3}) = [[∅], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

"""

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        subset = [[],[nums[0]]]
        if n==0 :
            return [[]]
        if n==1 :
            return subset
        if n>1 :
            for i in range(1,n):
                subset = subset * 2
                end = len(subset)
                mid = end // 2
                for j in range(mid,end):
                    subset[j] = subset[j] + [nums[i]]

        return subset


if __name__ == '__main__':
    nums = [1, 2, 3]
    sln = Solution()
    print(sln.subsets(nums))