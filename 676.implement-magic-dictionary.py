#
# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#
from typing import List

# class Trie(object):
#     def __init__(self):
#         self.trie = {}

#     def insert(self, word):
#         t = self.trie
#         for c in word:
#             if "-" in t:  return
#             elif c not in t: t[c] = {}
#             t = t[c]
#         t["-"] = word

#     def search_get_root(self, word):
#         t = self.trie
#         for c in word:
#             if "-" in t : return t["-"]
#             if c not in t: return None
#             t = t[c]
#         return t.get("-")

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.dictionary = set()

    def insert(self, word):
        if not word:
            return  
        t = self.trie
        for c in word:
            if c not in t: t[c] = {}
            t = t[c]
        t["-"] = t.get("-",0)  + 1    # mark for is word

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        if not dict: 
            return 
        self.dictionary = set(dict)

        for word in self.dictionary: 
            self.insert(word)
            for i in range(len(word)-1):
                self.insert(word[:i] + "*" + word[i+1:])
            self.insert(word[:len(word)-1]+ "*")
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        if not word: 
            return False

        find_words = [ word[:i] + "*" + word[i+1:]  for i in range(len(word)-1) ] 
        find_words.append(word[:len(word) -1] + "*")   

        for find_word in find_words:
            curr = self.trie
            is_search = True
            for ch in find_word: 
                if ch not in curr:
                    is_search = False
                    break
                curr = curr[ch]            
            if is_search and "-" in curr :
                if curr.get("-") > 1:
                    return True
                elif word not in self.dictionary:    
                    return True   
        return False
       
if __name__ == '__main__':
    md = MagicDictionary()
    md.buildDict(["hello", "leetcode"])
    print(md.search("hello"))               # F
    print(md.search("hhllo"))               # T
    print(md.search("hell"))
    print(md.search("leetcodeed"))

    # test 2 
    md.buildDict(["hello","hallo","leetcode"])


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

# '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n
# [[], [["hello","hallo","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]'

