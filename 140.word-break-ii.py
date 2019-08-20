#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
from typing import List 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {len(s) : ['']}
        wordDict = set(wordDict)                    # set run fast than list
        len_w = set(len(w) for w in wordDict)       # search space limit
        def sentences(i):
            if i not in memo: 
                memo[i] = [ 
                    s[i:i+j] + (tail and ' ' + tail)
                    for j in len_w
                    if s[i:i+j] in wordDict
                    for tail in sentences(i+j)      # iter
                ]
            return memo[i]
        return sentences(0)
    def wordBreak_1(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {len(s) :   ['']}
        def sentences(i):
            if i not in memo: 
                #   parameter and (" " + parameter)               
                # parameter - A1 is evaluated to True
                # result = (True and " " + parameter) 
                # result = (" " + parameter) 
                # parameter - A1 is evaluated to None
                # result = (None and " " + parameter) 
                # result = None 

                memo[i] = [ s[i:j] + (tail and ' ' + tail )   # comment up
                            for j in range(i+1, len(s) + 1)
                            if s[i:j] in wordDict
                            for tail in sentences(j)
                        ]
            return memo[i]
        return sentences(0)

    def wordBreak_wrong(self, s: str, wordDict: List[str]) -> List[str]:
        ans = [] 
        def dfs(s, wordDict, path):
            if not s :  
                ans.append(path[:])
                return 
            for i in range(1,len(s)):
                if s[:i] in wordDict:
                    dfs(s[i:], wordDict, path + [s[:i]])
        path = []
        dfs(s, wordDict, path)
        return ans 
        
if __name__ == '__main__':
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    sln = Solution()
    print(sln.wordBreak(s, wordDict))
    pass 
