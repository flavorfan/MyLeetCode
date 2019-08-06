#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
from typing import List
import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer, solutions, queen_positions = [], [], set()
        self.solveNQueensHelper( n, queen_positions, 0, solutions)

        for solution in solutions:
            board = [''] * n 
            for i in range(n):
                for j in range(n):
                    board[i] = board[i] + '.' if (i ,j) not in solution else board[i] + 'Q'
            answer.append(board)
        return answer

    def solveNQueensHelper(self, n, queen_positions, column, solutions):
        if column == n: 
            solutions.append(copy.copy(queen_positions))
        
        for row in range(n): 
            if self.isSafe((row, column), queen_positions):
                queen_positions.add((row, column))   # choose
                self.solveNQueensHelper(n, queen_positions, column + 1, solutions)
                queen_positions.remove((row, column)) # un-choose
    
    def isSafe(self, position, queen_positions):
        for queen in queen_positions:
            if (queen[0] == position[0] or abs(queen[1] - position[1]) == abs( queen[0] - position[0])):
                return False 
        return True 

            

if __name__ == '__main__':
    n = 4 
    sln = Solution()
    print( sln.solveNQueens(n))
    pass 
