#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# union find
# class UF:
#     def __init__(self,N):
#     def union(self,p,q): # initialize N sites with integer names
#     def find(self,p): #return component identifier for p
#     def connected(self,p,q): #return true if p and q are in the same component
#     def count(): #number of components

# https://www.jianshu.com/p/72da76a34db1



from typing import List
class Solution:
    def longestConsecutive_bruteforce(self, nums: List[int]) -> int:
        longest_steak = 0 
        for num in nums:
            current_num = num 
            current_steak = 1 
            while current_num + 1 in nums:
                current_num   += 1 
                current_steak += 1
            longest_steak = max(longest_steak, current_steak)
        return longest_steak

    # sort
    def longestConsecutive_sort(self, nums: List[int]) -> int:
        if not nums: 
            return 0 
        nums.sort()
        longest_steak = 1
        current_steak = 1  
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                if nums[i] == nums[i-1] + 1:
                    current_steak += 1 
                else: 
                    longest_steak = max(longest_steak, current_steak)
                    current_steak = 1
        return longest_steak
    
    # map
    def longestConsecutive_map(self, nums: List[int]) -> int:
        longest_steak = 0 
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_steak = 1
                while current_num + 1 in nums_set:
                    current_num += 1 
                    current_steak += 1 
                longest_steak = max(longest_steak, current_steak)
        return longest_steak

    # map improve
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        ans = 0
        for i in range(len(nums)):
            if nums[i] not in st:
                continue
            l = r = nums[i]
            st.remove(nums[i])
            while l-1 in st:
                l = l-1
                st.remove(l)
            while r+1 in st:
                r = r+1
                st.remove(r)
            ans = max(r-l+1, ans)
        return ans
    

        
if __name__ == '__main__':
    input = [100, 4, 200, 1, 3, 2]
    sln = Solution()
    print(sln.longestConsecutive(input))


