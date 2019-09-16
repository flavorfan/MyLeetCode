#
# @lc app=leetcode id=794 lang=python3
#
# [794] Valid Tic-Tac-Toe State
#
from typing import List
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        SIZE = 3
        turns = 0
        rows, cols = [0] * SIZE, [0] * SIZE
        diag1, diag2 = 0, 0 

        for i in range(SIZE):
            for j in range(SIZE):
                if board[i][j] == 'X':
                    turns += 1
                    rows[i] += 1
                    cols[j] += 1
                    if i == j: 
                        diag1 += 1
                    if i + j == SIZE - 1: 
                        diag2 += 1
                elif board[i][j] == 'O':
                    turns -= 1
                    rows[i] -= 1
                    cols[j] -= 1
                    if i == j: 
                        diag1 -= 1
                    if i + j == SIZE - 1:
                        diag2 -= 1
        wonX = (3 in rows) or (3 in cols) or diag1 == 3 or diag2 == 3
        wonO = (-3 in rows) or (-3 in cols) or diag1 == -3 or diag2 == -3

        if turns == 0 and not wonX or turns == 1 and not wonO:
            return True
        return False

if __name__ == '__main__':
    sln = Solution()
    board1 = ["O  ", "   ", "   "]
    print(sln.validTicTacToe(board1))
    board1 = ["XOX", " X ", "   "]
    print(sln.validTicTacToe(board1))
    board1 = ["XOX", "O O", "XOX"]
    print(sln.validTicTacToe(board1))
