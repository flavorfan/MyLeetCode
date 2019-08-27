#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#
from typing import List

class Trie(object):
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for c in word:
            if "-" in t:  return
            elif c not in t: t[c] = {}
            t = t[c]
        t["-"] = word

    def search_get_root(self, word):
        t = self.trie
        for c in word:
            if "-" in t : return t["-"]
            if c not in t: return None
            t = t[c]
        return t.get("-")


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dict:
            trie.insert(word)
        
        sentence_words = sentence.split(" ")
        for idx  in range(len(sentence_words)):
            replace_root = trie.search_get_root(sentence_words[idx])
            if replace_root:
                sentence_words[idx] = replace_root
        
        return " ".join(i for i in sentence_words)


if __name__ == '__main__':
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    sln = Solution()
    print(sln.replaceWords(dict,sentence))


