#
# @lc app=leetcode id=664 lang=python3
#
# [664] Strange Printer
#

# @lc code=start
import re 
import functools
class Solution:
    def strangePrinter(self, s: str) -> int:
        # Repeated element doesn't affect the final result. 
        # We remove all repeated elements.
        s = re.sub(r'(.)\1*', r'\1', s)
        @functools.lru_cache(None)
        def dp(i,j):
            if i>j:
                return 0
            res=dp(i+1,j)+1
            for k in range(i+1,j+1):
                if s[k]==s[i]:
                    res=min(res, dp(i,k-1)+dp(k+1,j))
            return res
        return dp(0,len(s)-1)    
class Solution2(object):
    def strangePrinter(self, s: str) -> int:
        string = []
        prev = ''
        for letter in s:
            if not prev:
                prev = letter
            elif letter == prev:
                continue
            elif letter != prev:
                string.append(prev)
                prev = letter
        string.append(prev)
        
        res = self.check(''.join(string),{}) 
        return res
    
    def check(self,s,memo):
        if s in memo:
            return memo[s]
        
        if not s:
            return 0
        
        res = self.check(s[:-1],memo) + 1
        for i in xrange(len(s) - 1):
            if s[i] == s[-1]:
                res = min(res,self.check(s[:i],memo) + self.check(s[i:- 1],memo))
        
        memo[s] = res
        return res    
# @lc code=end
if __name__ == '__main__':
    sln = Solution()
    s = 'aba'
    print(sln.strangePrinter(s))

