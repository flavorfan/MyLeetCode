#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

from typing import List


class Solution:
    def generateParenthesis_bruteforce(self, n: int) -> List[str]:
        def generate(A=[]):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A: List[str]) -> bool: 
            ballance = 0
            for c in A:
                if c == '(' : ballance += 1
                else: ballance -= 1
                if ballance < 0 : return False            
            return ballance == 0
        
        ans = []
        generate()
        return ans

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2*n:
                ans.append(S)            
            if left < n:
                backtrack(S + '(', left+1,right)
            if right < left:
                backtrack(S + ')', left, right+1)
        
        backtrack()
        return ans


if __name__ == '__main__' :
    n = 3
    sln = Solution()
    print (sln.generateParenthesis(n))
    pass
