#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List

class Solution: 
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}   

        def backtrack(combination,next_digits: str) -> List[str]:
            if len(next_digits) == 0:
                return self.ans.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combination+letter,next_digits[1:])

        self.ans = []
        if digits :
            backtrack("",digits)
        
        return self.ans

            
if __name__ == "__main__":
    digital =  "23"
    sln = Solution()
    print( sln.letterCombinations(digital))
    pass