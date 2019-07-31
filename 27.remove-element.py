#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            :param self: 
            :param nums:List[int]: 
            :param val:int: 
        """
        length = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[length] = nums[i]
                length += 1
        return length
        

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    sln = Solution()
    print(sln.removeElement(nums,val))