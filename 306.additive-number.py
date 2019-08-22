#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#
class Solution:
    def isValid(self, first, second, others):
        if (len(first) > 1 and first[0] == "0") or (len(second) > 1 and second[0] == "0"): 
            return False 
        sum_str = str(int(first) + int(second)) 
        if sum_str == others:
            return True
        elif others.startswith(sum_str):
            return self.isValid(second, sum_str, others[len(sum_str):])
        else: 
            return False
    def isAdditiveNumber_recurve(self, num: str) -> bool:
        length = len(num)
        for i in range(1, length // 2 + 1):            # search range 
            for j in range(1, (length-i) // 2 + 1 ):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if self.isValid(first, second, others): 
                    return True
        return False 
    
    def isAdditiveNumber(self, num: str) -> bool:
        length = len(num) 
        for i in range(1, length // 2 + 1):
            for j in range(1, (length - i) // 2 + 1) : 
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if (len(first) > 1 and first[0] == "0") or (len(second) > 1 and second[0] == "0"):
                    continue
                while others:
                    sum_str = str(int(first) + int(second))
                    if sum_str == others:
                        return True
                    elif others.startswith(sum_str):
                        first, second, others = second, sum_str, others[len(sum_str):]
                    else:  
                        break 
        return False 

if __name__ == '__main__':
    num = "0235813"
    sln = Solution()
    print(sln.isAdditiveNumber(num))

