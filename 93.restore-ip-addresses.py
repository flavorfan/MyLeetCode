#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = [] 
        def backtrack(comb, s, level):
            if (level == 0) and ( s == ""):
                ans.append(comb[:-1])
            elif (level != 0):
                for i in range(1, min(3+1, len(s) + 1)): 
                    if ( i > 1) and ( s[0] == '0'): 
                        continue
                    if ( 0 <= int(s[0:i]) <= 255 ): 
                        backtrack( comb + s[0:i] + '.', s[i:], level - 1)

        backtrack("", s, 4)
        return ans
        

if __name__ == '__main__':
    s = "25525511135"
    sln = Solution()
    print(sln.restoreIpAddresses(s))
    # pass 
