# Given n non-negative integers a1, a2, ..., an ,
# where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai)
# and (i, 0). Find two lines, which together with x-axis forms a container,
# such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        left = 0
        right = N-1

        ans = 0
        while left < right :
            # ans = max (ans, (r-left) * min(height[left],height[r]))
            if height[left] < height [right]:
                cur = height[left] * (right -left)
                left += 1
            else:
                cur = height[right] * (right - left)
                right -= 1
            ans = max(ans, cur)
        return ans

if __name__ == '__main__':

    A = [1,8,6,2,5,4,8,3,7]
    sln = Solution()
    ans = sln.maxArea(A)
    # Solution.maxArea(A)
    print(ans)
