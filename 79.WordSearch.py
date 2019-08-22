"""
79	Word Search
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,i,j,word):
                    return True
        return False

    def dfs(self,board,i,j,word):
        """
        :type board: List[List[str]]
        :type i: next loc row
        :type i: next loc col
        :type word: str
        :rtype: bool
        """
        # 1- return true result
        if len(word) == 0:
            return True
        # 2- early end
        if i<0 or i>= len(board) or j<0 or j>=len(board[0]) or board[i][j] !=  word[0] :
            return False
        # 3- backtrack tree fan out
        tmp = board[i][j]
        board[i][j] = "#"    # mark to be used
        res = self.dfs(board,i+1,j,word[1:]) or self.dfs(board,i-1,j,word[1:]) \
              or self.dfs(board,i,j+1,word[1:]) or self.dfs(board,i,j-1,word[1:])
        board[i][j] = tmp    # restore
        return res

if __name__ == '__main__':
    board = [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ]
    # word = "ABCCED"
    word = "ABCB"
    sln = Solution()
    print(sln.exist(board,word))
