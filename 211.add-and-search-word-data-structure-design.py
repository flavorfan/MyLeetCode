#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#
from collections import defaultdict
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words[len(word)].add(word)         # group
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        for other in self.words[len(word)]:
            # 用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True
            # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False
            any_mismatch = any( word[x] != '.' and word[x] != other[x] for x in range(len(word)))
            if not any_mismatch : 
                return True
        return False
        
if __name__ == '__main__':
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.search("pad"))
    print(wd.search("bad"))
    print(wd.search("mad"))
    print(wd.search(".ad"))
    print(wd.search("b.."))



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true

