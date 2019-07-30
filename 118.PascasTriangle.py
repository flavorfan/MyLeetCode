"""
118. Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for row_num in range(numRows):
            row = [1 for _ in range(row_num+1)]
            for j in range(1,len(row)-1):
                row[j] = ans[row_num-1][j-1] + ans[row_num-1][j]
            ans.append(row)
        return  ans

if __name__ == '__main__':
    numRows = 5
    sln = Solution()
    print(sln.generate(numRows))