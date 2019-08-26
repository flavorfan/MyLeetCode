#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#
from typing import List

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.val = None 
        self.chridren = {}

class Trie:
    def __init__(self):
        self.root = TrieNode() 
    def insert(self, word, idx):
        curr = self.root 
        for ch in word:  
            if ch not in curr.chridren:
                curr.chridren[ch] = TrieNode()
            curr = curr.chridren[ch]
        curr.isWord = True 
        curr.val = idx 
    def get_maxxor_from_search_inverse(self, word, nums, idx):
        curr = self.root
        comp = {'0':'1', '1':'0'} 
        for ch in word:
            if curr.chridren.get(comp[ch]):
                curr = curr.chridren[comp[ch]]
            else:   
                curr = curr.chridren.get(ch)
        return nums[curr.val] ^ nums[idx]


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0 
        trie = Trie() 
        nums_str = []
        for k, i in enumerate(nums):
            nums_str.append('{0:032b}'.format(i))
            # print('{0:032b} : {1}'.format(i,i))
            trie.insert(nums_str[-1],k)
        best = 0 
        for idx, w in enumerate(nums_str):
            best = max(best, trie.get_maxxor_from_search_inverse(w,nums,idx))
        return best
        
if __name__ == '__main__':
    nums = [3, 10, 5, 25, 2, 8]
    sln = Solution()
    # 5 :     101
    # 25 : 1 1001
    # 28 : 1 1100
    print(sln.findMaximumXOR(nums))
    #  ===============
    # method 1 1024ms 15.2%
    pass
