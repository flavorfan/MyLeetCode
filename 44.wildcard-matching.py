#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
import re 

class Solution:        
    def isMatch_new(self, s: str, p: str) -> bool:
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
    # 当pattern结束时若string还有剩余字符，仍然视为成功。想要完全匹配，可以在表达式末尾加上边界匹配符'$'
    def isMatch(self, s, p):
        parts = p.replace('?', '.').split('*')
        if len(parts) == 1:
            return bool(re.match(parts[0] + '$', s))
        if not re.match(parts[0], s):
            return False
        s = s[len(parts.pop(0)):]
        if not re.search(parts[-1] + '$', s):
            return False
        s = s[:len(s) - len(parts.pop())]
        for part in parts:
            m = re.search(part, s)
            if not m:
                return False
            s = s[m.end():]
        return True


if __name__ == "__main__":
    s = "aa"
    p = "a*"
    sln = Solution()
    print (sln.isMatch(s,p))

