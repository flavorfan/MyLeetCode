#
# @lc app=leetcode id=893 lang=python3
#
# [893] Groups of Special-Equivalent Strings
#

# @lc code=start
from typing import List
class Solution:
    # 表述一个特殊等价的字符串 SS
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)
        # 返回　52位编码的结构
        return len({count(word) for word in A})


        
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    A = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
    print(sln.numSpecialEquivGroups(A))
