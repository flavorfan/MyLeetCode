#
# @lc app=leetcode id=1032 lang=python3
#
# [1032] Stream of Characters
#
from typing import List
from collections import defaultdict

class StreamChecker_trie:
    def __init__(self, words: List[str]):
        self.root = {}
        self.q = []
        for word in words:
            curr = self.root
            for char in word:
                if char not in curr: 
                    curr[char] = {}
                curr = curr[char]
            curr['-'] = True

    def query(self, letter: str) -> bool:
        self.q.append(self.root)
        next_q = []
        for each in self.q:
            if letter in each: 
                next_q.append(each[letter])
        self.q = next_q
        return any([each.get('-') 
                    for each in self.q])


# Build a trie using the reversed words.
# Keep track of the queried letters.
# Check if the reverse of the queried string is in the trie.
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.flag = False
    
class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.history = []
        for word in words:
            node = self.trie
            for char in word[::-1]:
                node = node.children[char]
            node.flag = True

    def query(self, letter: str) -> bool:
        self.history.append(letter)
        node = self.trie
        for i in reversed(range(len(self.history))):
            if self.history[i] in node.children:
                node = node.children[self.history[i]]
                if node.flag: return True
            else: 
                return False
        return False                 

if __name__ == "__main__":
    words = ["cd","f","kl"]
    sk = StreamChecker(words)

    print(sk.query('a'))
    print(sk.query('b'))
    print(sk.query('c'))
    print(sk.query('d'))
    print(sk.query('e'))
    print(sk.query('f'))
    print(sk.query('g'))
    print(sk.query('h'))
    print(sk.query('i'))
    print(sk.query('j'))
    print(sk.query('k'))
    print(sk.query('l'))



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

