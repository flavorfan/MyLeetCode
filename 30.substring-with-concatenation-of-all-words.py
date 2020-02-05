#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from typing import List
class Solution:
    # 572ms 40.35%
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if not words or not s: 
            return res

        n = len(words[0])
        words_total_len = len(words) * n 
        sl = len(s)
        if words_total_len > sl : return res 
        words.sort()
        for i in range(sl-words_total_len+1):
            s1 = s[i:i + words_total_len] # slide window 
            s_temp = [s1[j:j+n] for j in range(0, len(s1), n)]
            s_temp.sort()
            if s_temp == words : 
                res.append(i)

        return res 
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(sln.findSubstring(s, words))
