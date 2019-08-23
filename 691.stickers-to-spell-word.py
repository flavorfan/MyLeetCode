#
# @lc app=leetcode id=691 lang=python3
#
# [691] Stickers to Spell Word
#
from collections import Counter
from typing import List

class Solution:
    # Optimized Exhaustive Search 
    def minStickers_exhaustive(self, stickers: List[str], target: str) -> int:
        t_counter = Counter(target)  # Counter 
        # print(t_counter)
        # ? counter &  intersection:  min(c[x], d[x]) # doctest: +SKIP ; c | d  union:  max(c[x], d[x])
        A = [ Counter(sticker) & t_counter for sticker in stickers] 
        # print(A)

        for i in range(len(A) - 1, -1, -1): 
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i!=j ): 
                A.pop(i)
        # print(A)

        self.best = len(target) + 1 

        def search( ans = 0):
            if ans > self.best: return 
            if not A: 
                if all( t_counter[letter] <= 0 for letter in t_counter ):
                    self.best = ans 
                return             
            sticker = A.pop() 
            # ! -> (x-1) // y 
            used = max(( t_counter[letter] - 1 ) // sticker[letter] + 1 for letter in sticker )
            used = max(used, 0)
            # search 
            for c in sticker:
                t_counter[c] -= used * sticker[c]           
            search( ans + used)
            for i in range(used - 1, -1, -1):
                for letter in sticker:
                    t_counter[letter] += sticker[letter]
                search( ans + i)    
            A.append(sticker)

        search()
        return self.best if self.best <= len(target) else -1 

    def minStickers(self, stickers: List[str], target: str) -> int:
        t_count = Counter(target)
        A = [Counter(sticker) & t_count for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)
        
        stickers = ["".join(s_count.elements()) for s_count in A ]
        # print(stickers) ['th', 'ea']
        
        dp = [-1] * ( 1 << len(target)) 
        dp[0] = 0 
        # update dp from small to large
        for state in range( 1 << len(target)):
            if dp[state] == -1: continue
            for sticker in stickers: 
                now = state 
                for letter in sticker: 
                    for i, c in enumerate(target): 
                        if (now >> i ) & 1 : continue  # if have allready fill 
                        if c == letter: 
                            now |= 1 << i 
                            break 
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1 
        return dp[-1]

    
      

if __name__ == '__main__':
    stickers = ["with", "example", "science"]
    target = "thehat"
    sln = Solution()
    print(sln.minStickers(stickers,target))
