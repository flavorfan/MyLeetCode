#
# @lc app=leetcode id=984 lang=python3
#
# [984] String Without AAA or BBB
#
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ans = []
        while A or B:
            if len(ans) >= 2 and ans[-2] == ans[-1]: 
                write_A = ans[-1] == 'b'
            else:
                write_A = A >= B 
            
            if write_A:
                ans.append('a')
                A -= 1
            else:
                ans.append('b')
                B -= 1
        return ''.join(ans)
        

if __name__ == '__main__':
    sln = Solution()
    print(sln.strWithout3a3b(2,3))
