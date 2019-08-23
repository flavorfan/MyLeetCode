#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#
class Solution:
    def dfs(self, idx, N, visited):
        if idx > N: 
            return 1 
        res = 0 
        for i in range(1, N+1):
            if visited[i]:
                continue 
            if i % idx == 0 or idx % i == 0:   
                visited[i] = True 
                res += self.dfs( idx + 1, N, visited) 
                visited[i] = False 
        return res 

    def countArrangement(self, N: int) -> int:
        visited = [False] * (N+1) 
        return self.dfs(1, N, visited)
        
if __name__ == '__main__':
    sln = Solution()
    print(sln.countArrangement(3))

