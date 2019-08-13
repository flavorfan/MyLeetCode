#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

from typing import List
import collections

class Solution:
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
    #     if endWord not in words: return [] 
    #     found, q, nq = False, {beginWord}, set() 
    #     while q and not found:
    #         words -= set(q)
    #         for x in q:
    #             for y in [x[:i] + c + x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm' ]:
    #                 if y in words: 
    #                     if y == endWord: found = True 
    #                 else: nq.add(y) 
    #                 tree[x].add(y) 
    #         q, nq = nq, set() 
    #     def bt(x):
    #         return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
    #     return bt(beginWord)

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
        while bq and not found:
            words -= set(bq)
            for x in bq:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y in eq: found = True
                        else: nq.add(y)
                        tree[y].add(x) if rev else tree[x].add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq): bq, eq, rev = eq, bq, not rev
        def bt(x): 
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        return bt(beginWord)

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    sln = Solution()
    print(sln.findLadders(beginWord,endWord,wordList))
    pass 