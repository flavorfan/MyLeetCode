#
# @lc app=leetcode id=488 lang=python3
#
# [488] Zuma Game
#

import collections
# @lc code=start
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        count = collections.Counter(hand)
        self.ans = len(hand) + 1

        def reduce(balls):
            i = 0
            for j, ball in enumerate(balls):
                if ball == balls[i]: continue 
                if j-i >= 3: return reduce (balls[0:i] + balls[j:])
                else:
                    i = j
            return balls 
        
        def dfs(remain):
            remain = reduce(remain)
            if remain == ['#']:
                self.ans = min(self.ans, len(hand) - sum(list(count.values())) )
            i = 0
            for j in range(len(remain)):
                if remain[i] == remain[j]:
                    continue
                need = 3 - ( j- i )
                if count[remain[i]] >= need:
                    count[remain[i]] -= need
                    dfs(remain[0:i] + remain[j:])
                    count[remain[i]] += need 
                i = j
        dfs(list(board + '#'))
        return -1 if self.ans > len(hand) else self.ans

# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    board, hand = "WWRRBBWW", "WRBRW"
    print(sln.findMinStep(board,hand))