#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 0:  
            return []
        nums = [i +1 for i in range(n)]
        used = [False for _ in range(n)]

        return self.__backtrack(nums, used, n, k, 0, [])
    def __factorial(self, n):
        res = 1 
        while n:
            res *= n 
            n -= 1 
        return res 
    
    def __backtrack(self, nums, used, n, k, depth, pre): 
        if depth == n: 
            return ''.join(pre)
        ps = self.__factorial(n-1 - depth)
        print(ps)
        for i in range(n):
            if used[i]:
                continue 
            if ps < k:
                k -= ps 
                continue 
            pre.append(str(nums[i]))
            used[i] = True 
            return self.__backtrack(nums, used, n, k, depth + 1, pre)

if __name__ == '__main__':
    n = 4 
    k = 9 
    sln = Solution()
    print(sln.getPermutation(n,k))

