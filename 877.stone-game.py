#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
from typing import List
from functools import lru_cache
class Solution:
    # dp 
    # 改变游戏规则，使得每当李2得分时，都会从亚历克斯1的分数中扣除。
    # 根据 dp(i + 1，j) 和 dp(i，j-1) 来制定 dp(i，j) 的递归，
    # 使用动态编程以不重复这个递归中的工作。该方法可以输出正确的答案，
    # 因为状态形成一个DAG（有向无环图）

    # dp 616ms 22.09%  
    def stoneGame_1(self, piles: List[int]) -> bool:
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

        return dp(0, N - 1) > 0

# 显然，亚历克斯总是赢得 2 堆时的游戏。 
# 通过一些努力，我们可以获知她总是赢得 4 堆时的游戏。
# 如果亚历克斯最初获得第一堆，她总是可以拿第三堆。 
# 如果她最初取到第四堆，她总是可以取第二堆。
# 第一 + 第三，第二 + 第四 中的至少一组是更大的，所以她总能获胜。
# 我们可以将这个想法扩展到 N 堆的情况下。
# 设第一、第三、第五、第七桩是白色的，第二、第四、第六、第八桩是黑色的。 
# 亚历克斯总是可以拿到所有白色桩或所有黑色桩，
# 其中一种颜色具有的石头数量必定大于另一种颜色的。
# 因此，亚历克斯总能赢得比赛。
    # 数学的方法


    def stoneGame(self, piles):
        return True
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    piles = [5,3,4,5]
    print(sln.stoneGame(piles))
