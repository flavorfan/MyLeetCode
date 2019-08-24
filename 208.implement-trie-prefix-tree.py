#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

class TrieNode:
    def __init__(self):
        self.isWord = False
        # self.word = ""
        self.chridren = {}

class Trie_old:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word: 
            if c not in cur.chridren:
                cur.chridren[c] = TrieNode() 
            cur = cur.chridren[c] 
        cur.isWord = True 
        cur.word = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word: 
            if c not in cur.chridren:
                return False 
            cur = cur.chridren[c]
        return cur.isWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root 
        for c in prefix:
            if c not in cur.chridren:
                return False 
            cur = cur.chridren[c]
        return True 

# advance : 1 - not need to create trie node class use dictionary
#           2 isWord by replace by add a '-' key to the dictionary 
class Trie(object):
    
	def __init__(self):
		self.trie = {}


	def insert(self, word):
		t = self.trie
		for c in word:
			if c not in t: t[c] = {}
			t = t[c]
		t["-"] = True


	def search(self, word):
		t = self.trie
		for c in word:
			if c not in t: return False
			t = t[c]
		return "-" in t

	def startsWith(self, prefix):
		t = self.trie
		for c in prefix:
			if c not in t: return False
			t = t[c]
		return True

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")

    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")   
    print(trie.search("app"))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


