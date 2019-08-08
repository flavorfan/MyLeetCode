#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(row, col):
            return not (rows[col] or hills[row - col] or dales[row + col] )

        def place_queen(row, col):
            rows[col] = 1 
            hills[row - col] = 1 
            dales[row + col] = 1 

        def remove_queen(row, col):
            rows[col] = 0 
            hills[row - col] = 0 
            dales[row + col] = 0
        
        def backtrack(row = 0, count = 0):
            for col in range(n):
                if is_safe(row, col):
                    place_queen(row, col)
                    if row + 1 == n: 
                        count += 1 
                    else: 
                        count = backtrack( row + 1, count)
                    remove_queen(row, col)
            return count 
    
        rows = [0] * n 
        hills = [0] * (2 * n -1)
        dales = [0] * (2 * n -1)
        return backtrack()

    # http://www.ic-net.or.jp/home/takaken/e/queen/
    def totalNQueens_bitmßap(self, n: int) -> int:
        def backtrack(row = 0, hills = 0, next_row = 0, dales = 0, count = 0):
            """
            :type row: 当前放置皇后的行号
            :type hills: 主对角线占据情况 [1 = 被占据，0 = 未被占据]
            :type next_row: 下一行被占据的情况 [1 = 被占据，0 = 未被占据]
            :type dales: 次对角线占据情况 [1 = 被占据，0 = 未被占据]
            :rtype: 所有可行解的个数
            """
            if row == n:  # 如果已经放置了 n 个皇后
                count += 1  # 累加可行解
            else:
                # 当前行可用的列
                # ! 表示 0 和 1 的含义对于变量 hills, next_row and dales的含义是相反的
                # [1 = 未被占据，0 = 被占据]
                free_columns = columns & ~(hills | next_row | dales)
                
                # 找到可以放置下一个皇后的列
                while free_columns:
                    # free_columns 的第一个为 '1' 的位
                    # 在该列我们放置当前皇后
                    curr_column = - free_columns & free_columns
                    
                    # 放置皇后
                    # 并且排除对应的列
                    free_columns ^= curr_column
                    
                    count = backtrack(row + 1, 
                                      (hills | curr_column) << 1, 
                                      next_row | curr_column, 
                                      (dales | curr_column) >> 1, 
                                      count)
            return count

        # 棋盘所有的列都可放置，
        # 即，按位表示为 n 个 '1'
        # bin(cols) = 0b1111 (n = 4), bin(cols) = 0b111 (n = 3)
        # [1 = 可放置]
        columns = (1 << n) - 1
        return backtrack()



if __name__ == '__main__':
    n = 4 
    sln = Solution()
    print(sln.totalNQueens_bitmßap(4))
        

