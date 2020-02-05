#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    # 20ms 97.97%
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1 
    '''
    # 36ms 37.78%
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        for j in range(len(haystack)):
            if j + len(needle) <= len(haystack) and haystack[j] == needle[0]:
                for i in range(len(needle)):
                    if haystack[j+i] != needle[i]:
                        break 
                else:
                    return j 
        return -1
    '''
    # 28ms 76.06%
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)
        total_step = haystack_len - needle_len + 1
        for i in range(total_step):
            if haystack[i:i+needle_len] == needle:
                return i 
        return -1 

        
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    print(sln.strStr("hello","ll"))

