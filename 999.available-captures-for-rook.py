#
# @lc app=leetcode id=999 lang=python3
#
# [999] Available Captures for Rook
#
from typing import List
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # print(sum(board,[]).index('R'))
        # concat the sublist to long list
        I, J = divmod(sum(board,[]).index('R'),8)
        C = "".join([i for i in [board[I]+['B']+[board[i][J] for i in range(8)]][0] if i != '.'])
        return C.count('Rp') + C.count('pR')
        

if __name__ == '__main__':
    sln = Solution()
    board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    print(sln.numRookCaptures(board))
