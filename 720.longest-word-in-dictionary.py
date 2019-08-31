#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#
from typing import List
import collections
from functools import reduce
# class Trie:
#     def __init__(self):
#         self.trie = {}
    
#     def insert(self, word):
#         curr = self.trie
#         for ch in word:
#             if ch not in curr: 
#                 curr[ch] = {}
#             curr = curr[ch]
#         curr['-'] = word
#     def search_longest(self):
#         candidate = ""
#         curr = self.trie
#         for ch in curr.keys():
#             if ch != '-' and '-' in curr[ch]:
#                 curr = curr[ch]
#                 if len(curr['-']) > len(candidate) or (len(curr['-']) == len(candidate) and curr['-'] > candidate):
#                     candidate = curr['-']        
#         return candidate

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # trie = Trie()
        # for word in words:
        #     trie.insert(word)      
        # return trie.search_longest()

        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        # important !!! beautiful implementation
        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        # important iterate  the trie tree 
        stack = list(trie.values())
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans

if __name__ == '__main__':
    # print("apply" > "apple")
    sln = Solution()
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(sln.longestWord(words))
