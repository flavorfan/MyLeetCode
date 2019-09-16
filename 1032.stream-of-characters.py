#
# @lc app=leetcode id=1032 lang=python3
#
# [1032] Stream of Characters
#
from typing import List
from collections import defaultdict
import collections

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
    
class StreamChecker_backtrie:
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

# Aho-Corasick
# https://en.wikipedia.org/wiki/Aho–Corasick_algorithm
# Each Trie node is implemented as a dictionary.
# The value at a character is the corresponding child node.
# The value at the special key 'prefix' is the target of the prefix pointer,
# and the value at 'dictionary' is the target of the dictionary pointer.
# If the node corresponds to a word in words, the node contains the key-value pair "word":True.
class StreamChecker:
    
    def __init__(self, words: List[str]):
        self.root = {'prefix': None, 'dict':None}
        
        #build Trie
        for word in words:
            node = self.root
            for char in word:
                if not char in node:
                    node[char] = {}
                node = node[char]
            node['word'] = True
                    
        #set prefix and dictionary pointers by BFS
        q = collections.deque([self.root])
        while q:
            node = q.popleft()
            for char in node:
                if len(char)==1:
                    child = node[char]
                    extendNode = node['prefix']
                    while extendNode and not char in extendNode:
                        extendNode = extendNode['prefix']
                    if extendNode:
                        child['prefix'] = extendNode[char]
                    else:
                        child['prefix'] = self.root
                    if 'word' in child['prefix']:
                        child['dict'] = child['prefix']
                    else:
                        child['dict'] = child['prefix']['dict']
                    q.append(child)
        
        #self.cur will traverse the Trie
        #while reading the stream
        self.cur = self.root

    def query(self, letter: str) -> bool:
        extendNode = self.cur
        while extendNode and not letter in extendNode:
            extendNode = extendNode['prefix']
        if extendNode:
            self.cur = extendNode[letter]
			#checks if current word is in words
			#or if the dictionary pointer is non-null
            if 'word' in self.cur or self.cur['dict']: 
                return True
            else:
                return False
        else:
            self.cur = self.root
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

