#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#

# @lc code=start
class Solution:
    # 892ms 20.66%
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal:
            return False
        
        if desiredTotal <= 0:
            return True
        
        bool_array = [i for i in range(1,maxChoosableInteger+1)]
        
        self.cache = {} 
        
        return self.minimax(desiredTotal,bool_array)
    
    def minimax(self,desiredTotal,visited):
        
        if tuple(visited) in self.cache:
            return self.cache[tuple(visited)]
        if desiredTotal <= 0:
            return False
        for i in range(len(visited)):
            temp = visited[i]
            newV = visited[:i] + visited[i+1:]
            if not self.minimax(desiredTotal-temp,newV):
                self.cache[tuple(visited)] = True
                return True
        self.cache[tuple(visited)] = False
        return False
        
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    print(sln.canIWin(10, 11))

