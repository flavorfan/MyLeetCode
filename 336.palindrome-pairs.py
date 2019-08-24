#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#
from typing import List 
from functools import reduce 
from collections import defaultdict

class Solution:
    def isPalin(self, s):
        return s == s[::-1]
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        root = {}
        for i, word in enumerate(words):
            curr = root 
            for idx, ch in enumerate(word):
                if ch not in curr: 
                    curr[ch] = {}
                curr = curr[ch]
                tmp = word[idx+1:]
                if tmp and self.isPalin(tmp):
                    # keep the idx of word if the suffix of the word after current position is palin
                    # curr.setdefault("ids", []).append(i)
                    if "ids" not in curr:
                        curr["ids"] = [i]
                    else: 
                        curr["ids"].append(i)
            curr["isWord"] = i # keep idx of word whetn reach the end 
        
        for j, word in enumerate(words):
            w = word[::-1] 
            curr = root 
            fail = False 
            for idx, ch in enumerate(w):
                if ch not in curr:  
                    fail = True 
                    break 
                curr = curr[ch] 
                # if current node is the end of some word, check whether the suffix of reverse word is palin
                i = curr.get("isWord") 
                if i is not None and i != j and self.isPalin(w[idx+1:]):
                    res.append([i, j])
            if not fail and "ids" in curr:
                res.extend( [i,j] for i in curr["ids"] if i != j)
            
        
        if "" in words: # check for ""case 
            idx = words.index("")
            res.extend(reduce(lambda x,y: x+y, ([[i, idx], [idx, i]] for i, w in enumerate(words) if w and self.isPalin(w))))

        return res 
        
if __name__ == '__main__':
    words = ["a","b","c","ab","ac","aa"] 
    sln = Solution()
    print( sln.palindromePairs(words))

