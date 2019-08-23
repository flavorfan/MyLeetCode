#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#
from typing import List
from collections import defaultdict 

class Solution:
    def readBinaryWatch_recurve(self, num: int) -> List[str]:
        ans = [] 
        def calcTime(arr):
            arr =  [str(i) for i in arr]
            return int("".join(arr), 2)  # int(x, base=10)
        def saveTime(h, m, ans):
            hour  = calcTime(h)
            mins  = calcTime(m)
            if hour <= 11 and mins <= 59 :
                ans.append(str(hour) + ":" + "{0:0>2}".format(mins))  # {:0>2d} 数字补零 (填充左边, 宽度为2)
        def dfs(arr, index, current, total):
            if current == total:
                saveTime(arr[0:4],arr[4:],ans)
                return 
            for i in range(index, 10):
                if 10 - index + current < total:
                    break 
                else:
                    arr[i] = 1 
                    dfs(arr, i+1, current + 1, total)
                    arr[i] = 0
        dfs( [0]*10, 0, 0, num)                         # creat 10 0 arrary
        return ans
    
    # pre-calc
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = defaultdict(list)
        mins = defaultdict(list)
        # count and store all hours '1'
        for i in range(12):
            bincount = bin(i)[2:].count('1')        # bin
            hours[bincount].append(i)
        
        for i in range(60):
            bincount = bin(i)[2:].count('1')
            mins[bincount].append(i)

        ans = []
        for i in range(num + 1):
            for hour in hours[i]:
                for min in mins[num-i]:
                    ans.append(str(hour) + ":" + "{0:0>2}".format(min))
        return ans 



        
if __name__ == '__main__':
    n = 1 
    sln = Solution()
    print(sln.readBinaryWatch(n))
