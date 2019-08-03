#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
from typing import List

class Solution:
    # ------- brute force -----------
    # def trap(self, height: List[int]) -> int:
    #     self.ans=0
    #     if len(height) == 0 :
    #         return self.ans           

    #     for i in range(1,len(height)-1) :
    #         max_left = max_right = 0
    #         for j in range(i,-1,-1): 
    #             max_left = max(max_left,height[j])
            
    #         for j in range(i,len(height)): 
    #             max_right = max(max_right, height[j])
            
    #         self.ans += (min(max_left,max_right) - height[i])
    #     return self.ans
    
    # -------- Dynamic programming ---------
    # def trap(self, height: List[int]) -> int:
    #     left = 0
    #     maxleft = height[:]
    #     for i in range(len(height)):
    #         maxleft[i] = left
    #         # left = max (left, height[i])
    #         if height[i] > left:
    #             left = height[i]
        
    #     right = 0 
    #     maxright = height[:]
    #     for i in range(len(height)-1,-1,-1):
    #         maxright[i] = right
    #         # right = max( right, height[i])
    #         if height[i] > right :
    #             right = height[i]

    #     res = 0
    #     for i in range(len(height)):
    #         # res += min( maxleft[i],maxright[i]) - height[i]
    #         if min(maxleft[i],maxright[i]) >  height[i]:
    #             res += min(maxleft[i],maxright[i]) - height[i]
    #     return res

    # def trap(self, height: List[int]) -> int:
    #     res, left_highest, right_highest, j = 0, [0]*len(height), [0]*len(height), len(height)-2
    #     for i in range(1, len(height)):
    #         left_highest[i] = max(left_highest[i-1], height[i-1])
    #         right_highest[j] = max(right_highest[j+1], height[j+1])
    #         j -= 1
    #     for i in range(1, len(height)-1):
    #         res += max(min(left_highest[i], right_highest[i]) - height[i], 0)
    #     return res

    #  ==== need to imply the stack  
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        stack = []
        for i in range(len(height)):
            while len(stack) != 0 and height[i] < height[stack[-1]]: 
                top = stack[-1]
                stack.pop()
                if len(stack) == 0:
                    break
                distance = i - stack[-1] - 1
                bound_height = min (height[i],height[stack[-1]]) - height[top]
                res += distance * bound_height
            stack.append(i)
        
        return res




if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    sln = Solution()
    print(sln.trap(height))
