#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#
class MapSum_my:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.trie['-'] = 0   # store the path sum
        # self.trie['*'] 

    def insert(self, key: str, val: int) -> None:
        curr = self.trie 
        # check for exist
        for ch in key:
            if ch not in curr: 
                curr[ch] = {}
                curr[ch]['-'] = 0
            curr = curr[ch]
            curr['-'] += val 
        if '*' not in curr:
            curr['*'] = val
        else:
            diff = curr['*']
            curr['*'] = val 

            curr = self.trie
            for ch in key:
                curr = curr[ch]
                curr['-'] -= diff



    def sum(self, prefix: str) -> int:
        curr = self.trie 
        for ch in prefix:
            if ch not in curr:  
                return 0 
            curr = curr[ch]
        return curr['-']

class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.next = {}

class MapSum(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        self.keys = {}          # important
        
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        i = 0
        while i < len(key):
            # add following nodes
            if key[i] not in node.next:
                node.next[key[i]] = Node()
            node = node.next[key[i]]
            # update existed key-value pair
            if key in self.keys:
                node.val += val - self.keys[key]
            else:
                node.val += val
            i += 1
        self.keys[key] = val
        
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        i = 0
        while i < len(prefix) and prefix[i] in node.next:
            node = node.next[prefix[i]]
            i += 1
        return node.val if i == len(prefix) else 0

if __name__ == '__main__':
    mapsum = MapSum()
    # mapsum.insert("apple",3)
    # print(mapsum.sum("ap"))        # 3
    # mapsum.insert("app",2)
    # print(mapsum.sum("ap"))        # 5  

    mapsum.insert("aa",3)
    print(mapsum.sum("a"))        # 3
    mapsum.insert("aa",2)
    print(mapsum.sum("a"))        # 2 

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

