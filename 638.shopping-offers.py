#
# @lc app=leetcode id=638 lang=python3
#
# [638] Shopping Offers
#

# @lc code=start
from typing import List
import functools
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n=len(price)
        # tmp = special saved
        tmp=[sum(s[i]*price[i] for i in range(n))-s[-1] for s in special]
        # print(special)
        for i in range(len(special)):
            special[i][-1]=tmp[i]
        special=[s for s in special if s[-1]>0]
        special.sort(key=lambda x: x[-1],reverse=True)
        # print(special)
        # python for-else
        @functools.lru_cache(None)
        def dfs(rest):
            res=0
            for s in special:
                tmp=[]
                # try add cur special
                for i in range(n):
                    if rest[i]<s[i]:
                        break
                    tmp.append(rest[i]-s[i])
                else:
                    # cur saved ++
                    cur = dfs(tuple(tmp)) + s[-1]
                    res = max(res,cur)
            return res

        saved   = dfs(tuple(needs))
        unsaved = sum(price[i]*n for i,n in enumerate(needs))
        return unsaved - saved
        
# @lc code=end

if __name__ == '__main__':
    price = [2,5]
    special = [[3,0,5],[1,2,10]]
    needs = [3,2]
    sln = Solution()
    print(sln.shoppingOffers(price, special, needs))