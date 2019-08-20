#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

from typing import List
import collections

class Solution:
    def findLadders_old(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        # 1- concreate the search tree 
        # not "seen" set but a more like "explored" set. 
        found, q, nq = False, {beginWord}, set()
        while q and not found:
            words -= set(q)
            for x in q:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y == endWord: found = True
                        else: nq.add(y)
                        tree[x].add(y)
            q, nq = nq, set()
        # 2- bfs
        def bt(x): 
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        return bt(beginWord)    

    # single directional BFS which cost more than 2500ms. 
    # BFS't time complexity is O(b^d) where b is branch factor and d is depth. 
    # bi-directional BFS reducing running time from 2500ms to 100ms!
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
        while bq and not found:
            words -= set(bq)
            for x in bq:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y in eq: found = True    # important 
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
    print(sln.findLadders_old(beginWord,endWord,wordList))
    pass 