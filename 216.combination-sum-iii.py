#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
from typing import List
import itertools
class Solution:
    def __dfs(self, start, path,  residuce_sum, residuce_cnt):
        if residuce_sum == 0 and residuce_cnt == 0:
            self.ans.append(path[:])
            return 
         
        for num in range(start, 10):
            if num > residuce_sum or residuce_cnt < 1: 
                break
            path.append(num)
            self.__dfs(num+1, path,residuce_sum - num, residuce_cnt - 1)
            path.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.__dfs(1,[],n,k)
        return self.ans
    
    def combinationSum3_new(self, k: int, n: int) -> List[List[int]]:
        res=[] 
        # 1 itertools.combinations 用于求序列的组合
        # [(n1..nk),()]
        # 2 map set to list
        lst=list(map(list,list(itertools.combinations([x for x in range(1,10)], k))))
        # print(lst) 
        res=[x for x in lst if sum(x)==n]
        return res


if __name__ == '__main__':
    k, n = 3, 9 
    sln = Solution()
    print(sln.combinationSum3(k,n))
