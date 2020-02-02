#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    # slide windows / two point
    # 64ms 61.04%
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        p1 = p2 = m = 0
        while p2 < len(s):
            if s[p2] not in d:
                d[s[p2]] = True
                p2 += 1
                m = max(len(d), m)
            else:
                del d[s[p1]]
                p1 += 1
        return m 
    """
    # 44ms 97.66%
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        max_len = cur_len = 0
        
        for ch in s:
            if ch in sub:
                index = sub.index(ch)
                sub = sub[index+1:]
                cur_len = len(sub)
            sub += ch
            cur_len += 1
            if max_len < cur_len:
                max_len = cur_len
        
        return max_len

        
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    print(sln.lengthOfLongestSubstring("abcabcdaf"))