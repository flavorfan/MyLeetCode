#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
from typing import List
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click[0], click[1]
        # check if x,y in board
        if not ( 0 <= x < len(board) and 0 <= y < len(board[0])):
            return 
        
        # situatin 1 
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        elif board[x][y] == 'E':
            num_adj_mines = self.has_adj_mines(board, x, y)

            # situation 3
            if num_adj_mines:
                board[x][y] = str(num_adj_mines)
            
            # situation 2
            else:
                board[x][y] = 'B'
                self.updateBoard(board, [x + 1, y])
                self.updateBoard(board, [x, y + 1])
                self.updateBoard(board, [x - 1, y])
                self.updateBoard(board, [x, y - 1])
                self.updateBoard(board, [x + 1, y + 1])
                self.updateBoard(board, [x + 1, y - 1])
                self.updateBoard(board, [x - 1, y + 1])
                self.updateBoard(board, [x - 1, y - 1])
            return board
        
    def has_adj_mines(self, board, x, y):
        def is_mine(x,y):
            if not ( 0 <= x < len(board) and 0 <= y < len(board[0])):
                return 0
            if board[x][y] == 'M':
                return 1
            return 0
        num_adj_mines = is_mine(x+1, y) + is_mine(x-1, y) + is_mine(x, y+1) + is_mine(x, y-1) + is_mine(x+1, y+1) + is_mine(x+1, y-1) + is_mine(x-1, y+1) + is_mine(x-1, y-1)
        return num_adj_mines
# @lc code=end

if __name__ == '__main__':
    board = [['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'M', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E']]
    clk = [3,0]
    sln = Solution()
    print(sln.updateBoard(board, clk))

