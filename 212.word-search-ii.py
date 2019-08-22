#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
from typing import List

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.word = ""
        self.chridren = {}
    
    def constructWord(self, word):
        cur = self 
        for c in word: 
            if c not in cur.chridren:
                cur.chridren[c] = TrieNode() 
            cur = cur.chridren[c] 
        cur.isWord = True 
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.constructWord(word)
        res = [] 
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [ [False] * n for _ in range(m)]      # record the path

        def dfs(node, x, y):
            if node.isWord:
                res.append(node.word)
                node.isWord = False   # not find again 
            visited[x][y] = True 
            for dire in directions:
                x2, y2 = x + dire[0], y + dire[1]
                if 0 <= x2 < m and 0 <= y2 < n and board[x2][y2] in node.chridren and not visited[x2][y2]:
                    dfs(node.chridren[board[x2][y2]], x2, y2)   # explore the next 
            
            visited[x][y] = False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.chridren:
                    dfs(root.chridren[board[i][j]], i, j)
        
        return res

if __name__ == '__main__':
    board = [
                ['o','a','a','n'],
                ['e','t','a','e'],
                ['i','h','k','r'],
                ['i','f','l','v']
            ]
    words = ["oath","pea","eat","rain"]
    sln = Solution()
    print( sln.findWords(board, words))
