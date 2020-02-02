#
# @lc app=leetcode id=546 lang=python3
#
# [546] Remove Boxes
#
# https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-546-remove-boxes/
# @lc code=start
from typing import List 
from collections import defaultdict
# import collections 
# 268ms
# ToDo ? hash map
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        self.ans = 0
        # count = collections.Counter(boxes)
        N = len(boxes)
        self.boxes = boxes
        self.dp = [[[0]* N for _ in range(N)] for _ in range(N)]
        return self.dfs(0,N-1,0)

    def dfs(self, l, r , k):
        if (l > r): return 0
        if (self.dp[l][r][k] > 0):
            return self.dp[l][r][k]
        while l < r and self.boxes[r] == self.boxes[r-1]:
            r -= 1
            k += 1
        
        # case 1
        self.dp[l][r][k] = self.dfs(l, r-1, 0) + (k + 1) ** 2

        # case 2
        for i in range(l,r):
            if self.boxes[i] == self.boxes[r]:
                # ? 
                self.dp[l][r][k] = max(self.dp[l][r][k], self.dfs(l, i, k+1) + self.dfs(i+1, r-1, 0))
        
        return self.dp[l][r][k]

# top - down dp
class Solution_topdown:
    def removeBoxes(self, boxes: List[int]) -> int:    
        N = len(boxes)
        self.boxes = boxes
        self.dp = [[[0]* N for _ in range(N)] for _ in range(N)]
        return self.search(0, N-1, 0)
        
    def search(self, l, r, k):
        if l > r:
            return 0
        
        if self.dp[l][r][k] != 0:
            return self.dp[l][r][k]
        
        while l < r and self.boxes[r] == self.boxes[r-1]:
            r -= 1
            k += 1
            
        self.dp[l][r][k] = self.search(l, r-1, 0) + (k + 1) * (k + 1)
        
        for i in range(l, r):
            if self.boxes[i] == self.boxes[r]:
                self.dp[l][r][k] = max(self.dp[l][r][k], self.search(l,i,k+1)+self.search(i+1,r-1,0))
                
        return self.dp[l][r][k]

class Solution_2:
    def removeBoxes(self, boxes):
        if not boxes:
            return 0
        # tmp    counters
        tmp = []
        color, count = boxes[0], 1
        for i in range(1, len(boxes)):
            if color != boxes[i]:
                tmp.append([color, count])
                color, count = boxes[i], 1
            else:
                count += 1
        tmp.append([color, count])

        # 
        lst_index = defaultdict(list)
        dt_index = defaultdict(dict)
        for i in range(len(tmp)):
            lst_index[tmp[i][0]].append(i)
            dt_index[tmp[i][0]][i] = len(lst_index[tmp[i][0]]) - 1

        # dfs memo
        memo = {}
        def helper(i, j, k):
            if i > j:
                return 0
            if i == j:
                return k * k
            if (i, j, k) in memo:
                return memo[i, j, k]
            res = k * k + helper(i, j - 1, tmp[j - 1][1])

            ttt = lst_index[tmp[j][0]]
            iii = dt_index[tmp[j][0]][j] - 1
            while iii >= 0 and ttt[iii] >= i:
                idx = ttt[iii]
                res = max(res, helper(i, idx, tmp[idx][1] + k) + helper(idx + 1, j - 1, tmp[j - 1][1]))
                iii -= 1
            memo[i, j, k] = res
            return res

        return helper(0, len(tmp) - 1, tmp[-1][1])
        
# @lc code=end

if __name__ == '__main__':
    boxes = [6, 10, 1, 7, 1, 3, 10, 2, 1, 3]
    sln = Solution()
    print(sln.removeBoxes(boxes))

