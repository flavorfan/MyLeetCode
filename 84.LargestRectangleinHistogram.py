"""
84. Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.
Example:

Input: [2,1,5,6,2,3]
Output: 10
持续弹栈来计算从栈顶点到降序点的矩阵大小

用递增栈，还是用递减栈来做
递增栈是维护递增的顺序，当遇到小于栈顶元素的数就开始处理，
而递减栈正好相反，维护递减的顺序，当遇到大于栈顶元素的数开始处理。

因此我们需要一个递增栈，当遇到大的数字直接进栈，而当遇到小于栈顶元素的数字时，
就要取出栈顶元素进行处理了，

"""
class Solution:
    def largestRectangleArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n==0:
            return 0
        max_area = 0
        for i in range(n):
            for j in range(i,n):
                # minist in i j
                min_len = min(heights[i:j+1])
                max_area = max(max_area, min_len * (j-i+1) )
        return max_area

    # Mono Stack
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        res = 0
        stack = []
        heights.append(-1)
        for i in range(len(heights)):
            current = heights[i]
            while len(stack) != 0 and current <= heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if len(stack) == 0 else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res



if __name__ == '__main__':
    # heights = [2,1,5,6,2,3] # 10
    heights = [2,1,2]
    # heights = [0, 9]  # 10
    sln = Solution()
    print(sln.largestRectangleArea3(heights))
