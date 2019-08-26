#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#
from typing import List
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if len(word) == 0: return
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

    def search(self, word):
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if node is None:
                return False
        return node.isWord

class Solution:
    # dfs
    def findAllConcatenatedWordsInADict_dfs(self, words: List[str]) -> List[str]:
        ans = [] 
        self.wordSet = set(words)
        for word in words:
            self.wordSet.remove(word)               # important
            if self.search_dfs(word):
                ans.append(word[:])
            self.wordSet.add(word)
        return ans 
    def search_dfs(self, word):
        if word in self.wordSet: 
            return True 
        for idx in range(1, len(word)):
            if word[:idx] in self.wordSet and self.search_dfs(word[idx:]):
                return True 
        return False 
    

    # Trie 
    # need to test "" case 
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.trie = Trie()
        ans = []
        for word in words:
            self.trie.insert(word)
        for word in words:
            if self.search(word):
                ans.append(word)
        return ans

    def search(self, word):
        node = self.trie.root
        for idx, letter in enumerate(word):
            node = node.children.get(letter)
            if node is None:
                return False
            suffix = word[idx+1:]
            if node.isWord and (self.trie.search(suffix) or self.search(suffix)):
                return True
        return False

    # def findAllConcatenatedWordsInADict_my(self, words: List[str]) -> List[str]:
    #     root = {}
    #     ans = []
    #     words.sort(key = len)
    #     for idx, word in enumerate(words):
    #         curr = root 
    #         for ch in word:
    #             if ch not in curr:  
    #                 curr[ch] = {}
    #             curr = curr[ch]
    #         curr['-'] = idx 
        
    #     # search trie tree 
    #     def isConcatenated(word,i):
    #         if  len(word) == 0 and i > 1:
    #             return True          
    #         curr = root
    #         for idx, ch in enumerate(word):
    #             if curr.get('-') :
    #                 return isConcatenated(word[idx+1:],i+1)
    #             if ch not in curr:
    #                 return False 
    #             curr = curr[ch]
    #         return  ('-' in curr) and ( i > 1) 
        
        # for idx, word in enumerate(words):
        #     curr = root 
        #     concatenated_num = 0
        #     for ch in word:
        #         if curr.get('-') and curr.get('-') != idx: 
        #             concatenated_num += 1
        #             if ch not in curr:
        #                 break
        #             curr = root[ch]
        #         else:     
        #             if ch not in curr:
        #                 break           
        #             curr = curr[ch]
        #     if curr.get('-') and  concatenated_num > 1: 
        #         ans.append(words[idx][:])       
        # return ans      

if __name__ == '__main__':
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    sln = Solution() 
    print(sln.findAllConcatenatedWordsInADict(words))