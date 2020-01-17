#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#
# 给一个数字 nn ，我们要用最优策略在  
# (1, n)(1,n) 范围内考虑猜中数字的最坏情况
# cost(1,n)=i+max(cost(1,i−1),cost(i+1,n))
# @lc code=start
class Solution:
    # 248ms 88.84% 
    # 暴力解法　＋　改善搜索空间　＋　ＤＰ　
    def getMoneyAmount(self, n: int) -> int:
        mem={}

        def calculate(l,h):
            if l >= h:  return 0
            if (l,h) not in mem:
                mem[l,h] = min(i + max(calculate(i+1, h), calculate(l, i-1)) for i in range((l+h)>>1, h+1))
            return mem[l,h]

        return calculate(1,n)
            
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    print(sln.getMoneyAmount(10))

