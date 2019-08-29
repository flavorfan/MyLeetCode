#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#
class MapSum:

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

