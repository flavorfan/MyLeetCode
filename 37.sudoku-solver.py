#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#


from typing import List

class Solution:
    col_size = 9  # len(self.board)
    row_size = 9  # len(self.board[0])
    block_col_size = 3
    block_row_size = 3
    digits = '123456789'
    empty_symbol = '.'

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Algorithm: backtracking (dfs) in an optimal order
        1,Keep track of candidates of each cell.
        2,Find the cell with fewest candidates. Fill the cell with one of the candidates. Update the candidates of other cells.
        3,Repeat step 2 until solved. Or if the board is not solvable anymore (there's any cell that is empty but has no candidates), undo step 2 and try the next candidate.
        """
        self.init(board)
        self.solve()

    def init(self, board):
        self.board = board
        # list all empty cells. a `cell` is a tuple `(row_index, col_index)`
        self.empty_cells = set([
            (ri, ci) for ri in range(self.row_size) 
            for ci in range(self.col_size) 
            if self.board[ri][ci] == self.empty_symbol
            ])

        # find candidates of each cell
        self.candidates = [[set(self.digits) for ci in range(self.col_size) ] for ri in range(self.row_size)]
        for ri in range(self.row_size):
            for ci in range(self.col_size):
                digit = self.board[ri][ci]
                if digit != self.empty_symbol:
                    self.candidates[ri][ci] = set()
                    self.update_candidates((ri,ci),digit)
    
    def solve(self):
        # if there are no empty cells, it's solve
        if not self.empty_cells:
            return True
        
        # get cell with fewest candidates
        cell = min( self.empty_cells, key = lambda cell: len(self.candidates[cell[0]][cell[1]]) )

        # try to fill the cell with one of candidates, and solve recursivity
        ri,ci = cell
        for digit in list(self.candidates[ri][ci]):
            candidates_updated_cell = self.fill_cell(cell,digit)
            solved = self.solve()
            if solved:
                return True
            self.unfill_cell(cell, digit, candidates_updated_cell)
        
        # if no solutin found, go back and try next candidate
        return False
    
    def fill_cell(self, cell, digit):
        ri, ci = cell
        self.board[ri][ci] = digit

        self.empty_cells.remove(cell)
        candidates_updated_cell = self.update_candidates(cell,digit)

        return candidates_updated_cell
    
    def unfill_cell(self, cell, digit, candidates_updated_cell):
        ri, ci = cell
        self.board[ri][ci] = self.empty_symbol

        self.empty_cells.add(cell)

        for ri,ci in candidates_updated_cell:
            self.candidates[ri][ci].add(digit)

        
    def update_candidates(self, filled_cell, digit):
        candidates_updated_cell = []
        for ri,ci in self.related_cells(filled_cell):
            if (self.board[ri][ci] == self.empty_symbol) and (digit in self.candidates[ri][ci]):
                self.candidates[ri][ci].remove(digit)
                candidates_updated_cell.append((ri,ci)) 
        return candidates_updated_cell
    
    def related_cells(self,cell):
        return list(set(self.cells_in_same_row(cell) + self.cells_in_same_col(cell) + self.cells_in_same_block(cell) ))


    def cells_in_same_row(self, cell):
        return [ (cell[0],ci) for ci in range(self.col_size)]

    def cells_in_same_col(self, cell):
        return [(ri, cell[1]) for ri in range(self.row_size)]
    
    def cells_in_same_block(self, cell):
        block_first_cell_ri = cell[0] // self.block_row_size * self.block_row_size
        block_first_cell_ci = cell[1] // self.block_col_size * self.block_col_size
        return [
            (block_first_cell_ri + in_block_ri, block_first_cell_ci + in_block_ci)
            for in_block_ri in range(self.block_row_size)
            for in_block_ci in range(self.block_col_size)
        ]





if __name__ == "__main__" :
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    sln = Solution()
    sln.solveSudoku(board)
    print(sln.board)
    # pass    

