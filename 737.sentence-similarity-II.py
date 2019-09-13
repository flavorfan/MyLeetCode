# @lc app=leetcode id=721 lang=python3

# Given two sentences words1, words2 (each represented as an array of strings), 
# and a list of similar word pairs pairs, determine if two sentences are similar.
# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, 
# if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

# Note that the similarity relation is transitive. 
# For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

# Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

# Note:

# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].

# 用int当索引效率更高，
# 更优雅的实现用一个  word_to_id (dict)
from typing import List

class Solution(object):
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        root = {}
        # xp = x/parent(x)
        def find(x):
            p = root.setdefault(x,x)
            if x != p:
                r = find(p)
                root[x] = r
            return root[x]
        
        # 
        def union(x, y):
            xp, yp = find(x), find(y)
            if xp != yp:
                root[xp] = root[yp]
        
        for pair in pairs:
            union( pair[0], pair[1])
        
        return any( find(w1) == find(w2) for w1, w2 in zip(words1, words2))


if __name__ == '__main__':
    sln = Solution()
    words1 = ["great", "acting", "skills"] 
    words2 = ["fine", "drama", "talent"]
    pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]

    print(sln.areSentencesSimilarTwo(words1, words2, pairs))
