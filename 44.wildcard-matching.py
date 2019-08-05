#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

class Solution:        
    def isMatch(self, s: str, p: str) -> bool:
        def find(s,p):
            for i in range(len(s) - len(p) + 1):
                if all(p[j] in (s[i+j], '?') for j in range(len(p))):
                    return i
            return -1 
    
        # ? *abcd* parts ?
        parts = p.split('*')
        if len(parts) == 1:
            return len(s) == len(p) and find(s,p) >= 0 
        
        if find(s, parts[0]) != 0:
            return False 
        
        s = s[len(parts.pop(0)):]
        n = len( s ) - len( parts[-1]) 
        if find( s[n: ],parts.pop()) != 0:
            return False 
        
        s = s[:n]
        for part in parts:
            index = find(s,part)
            if index < 0: 
                return False
            s = s[index + len(part):]
        
        return True 



if __name__ == "__main__":
    s = "aa"
    p = "a*"
    sln = Solution()
    print (sln.isMatch(s,p))

