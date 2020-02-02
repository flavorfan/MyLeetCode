#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#
# 一个运算符一定会跟随一对括号，比如 (t)(t)。
# 所以我们可以直接判断 expression[0]，得到最外层的运算符，根据运算符处理内层的表达式。

# 如果不是运算符，肯定就是 t 或者 f 直接判断即可

# 如果是 !!，里面要么就是单一的字符，要么就是一个新的表达式。
# 再调用 parseBoolExpr 解析并取反即可。
# 如果是 & 或者 |∣， 需要对里面每个表达式分别求解。
# 通过括号匹配，拿到第一个 ( 匹配的 ) 里面的表达式，再通过 parseBoolExpr 计算出值。
# 在计算 & 的时候，如果有一个值为 false，可以提前结束计算。
# 同理，在计算 |∣ 时， 如果有一个值为 true，也可以提前结束计算。

# "t"，运算结果为 True
# "f"，运算结果为 False
# "!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
# "&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
# "|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）


# @lc code=start
class Solution:
    # 整体框架：递归 backtrace?
    # 60ms 63.91%
    def parseBoolExpr(self, expression: str) -> bool:
        if expression == 't':
            return True
        if expression == 'f':
            return False
        if expression[0] == '!':
            return not self.parseBoolExpr(expression[2:-1])
        
        exp_lists = []
        
        # Create the list of Inner Expressions
        # &(t,t,t)
        # use to compute bracket cout
        open_bracket = 0
        prev = 2
        for i in range(2,len(expression)):
            if expression[i] == ',' and open_bracket == 0:
                exp_lists.append(expression[prev:i])
                prev = i+1
            elif expression[i] == '(':
                open_bracket+=1
            elif expression[i] == ')':
                open_bracket-=1
        exp_lists.append(expression[prev:-1])

	   # Evaluate the answer
	   
        for i in exp_lists:
            val = self.parseBoolExpr(i)
            if val == False and expression[0] == '&':
                return False
            if val == True and expression[0] == '|':
                return True
            
        if expression[0] == '&':
            return True
        if expression[0] == '|':
            return False

        
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    expression = "!(f)"
    print(sln.parseBoolExpr(expression))
