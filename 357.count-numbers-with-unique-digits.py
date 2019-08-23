#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        ans, muls = 10 ,9 
        for i in range(1, min(n,10)):
            muls *= 10 - i 
            ans += muls
        return ans 
        

if __name__ == '__main__':
    n = 2 
    sln = Solution() 
    print(sln.countNumbersWithUniqueDigits(n))
    pass