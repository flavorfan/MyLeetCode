#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                temp_list = []
                t = stack.pop()
                while  t!= '[' and len(stack) != 0:
                    temp_list.append(t)
                    t=stack.pop()
            
                num = stack.pop()
                while len(stack)>0:
                    if stack[-1].isdigit():
                        num+=stack.pop()
                    else:
                        break
                        
                num= num[::-1]
                temp_list.reverse()

                temp_list = temp_list * int(num)
                for i in temp_list:
                    stack.append(i)
        res ="".join(stack)

        return res
# @lc code=end

