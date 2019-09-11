#
# @lc app=leetcode id=770 lang=python3
#
# [770] Basic Calculator IV
#
# 在这道题目中，我们需要使用两个栈：主栈和操作符栈。
# 我们线性扫描expression，并对遇到的变量、常量、操作符进行入栈或者其他的操作。

# 对于主栈，我们可以：

# 将变量或常量压入栈中；
# 将栈顶两个元素弹出，并进行某种运算（加、减、乘）后，将结果压入栈中。
# 对于操作符栈，我们可以：

# 将栈顶元素弹出；
# 将操作符压入栈中。
# 注意，仅当操作符栈为空，或者栈顶元素的优先级低于想要入栈的元素时，才可以进行压栈操作。否则，我们需要将栈顶元素弹出，直到满足压栈条件为止。操作符的优先级如下：( < ) < + = - < *。还需要注意的是，
# （1）(无条件入栈的，以保证括号的优先级最高。
# （2）遇到)时，我们将栈顶元素弹出，直到弹出(为止，并且)本身不进入栈中。
#  
from typing import List
import collections
import re 
class Poly(collections.Counter):
    # overide + operator
    # 可以使用一个iterable对象或者另一个Counter对象来更新键值。
    def __add__(self, other):
        self.update(other)
        return self
    
    def __sub__(self, other):
        self.update({k: -v for k,v in other.items()})
        return self
    
    def __mul__(self, other):
        product = Poly()
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                product.update({tuple(sorted(k1 + k2)): v1 * v2})
        return product
    
    def evaluate(self, evalmap):
        ans = Poly()
        for k, c in self.items():
            free = []
            for token in k:
                if token in evalmap:
                    c *= evalmap[token]
                else:
                    free.append(token)
            ans[tuple(free)] += c
        return ans

class Solution2:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        evalmap = zip(evalvars, evalints)

        def combine(left, right, symbol):
            if symbol == '+': return left + right
            if symbol == '-': return left - right
            if symbol == '*': return left * right
            raise

        def make(expr):
            ans = Poly()
            if expr.isdigit():              # is number
                ans.update({(): int(expr)})
            else:
                # ?
                ans[(expr,)] += 1
            return ans
        
        def parse(expr):
            bucket = []
            symbols = []
            i = 0
            while i < len(expr):
                if expr[i] == '(': 
                    bal = 0
                    for j in range(i,len(expr)):
                        if expr[j] == '(': bal += 1
                        if expr[j] == ')': bal -= 1
                        if bal == 0: break
                    bucket.append(parse(expr[i+1:j]))
                    i = j
                elif expr[i].isalnum():
                    for j in range(i, len(expr)):
                        if expr[j] == ' ': 
                            bucket.append(make(expr[i:j]))
                            break
                    else:
                        bucket.append(make(expr[i:]))
                    i = j
                elif expr[i] in '+-*': 
                    symbols.append(expr[i])
                i += 1
            
            for i in range(len(symbols) - 1 , -1, -1):
                if symbols[i] == '*': 
                    bucket[i] = combine(bucket[i], bucket.pop(i+1), symbols.pop(i))
            if not bucket: return Poly() 
            ans = bucket[0]

            for i, symbol in enumerate(symbols, 1):
                ans = combine(ans, bucket[i], symbol)

            return ans

        P = parse(expression).evaluate(evalmap)
        return P.to_list()    

class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        class C(collections.Counter):
            def __add__(self, other):
                self.update(other)
                return self
            def __sub__(self, other):
                self.subtract(other)
                return self
            def __mul__(self, other):
                product = C()
                for x in self:
                    for y in other:
                        xy = tuple(sorted(x + y))
                        product[xy] += self[x] * other[y]
                return product
        vals = dict(zip(evalvars, evalints))
        def f(s):
            s = str(vals.get(s, s))
            return C({(s,): 1}) if s.isalpha() else C({(): int(s)})
        c = eval(re.sub('(\w+)', r'f("\1")', expression))
        return ['*'.join((str(c[x]),) + x)
                for x in sorted(c, key=lambda x: (-len(x), x))
                if c[x]]
        
if __name__ == '__main__':
    sln = Solution()
    expression = "e + 8 - a + 5"
    evalvars = ["e"]
    evalints = [1]
    print(sln.basicCalculatorIV(expression, evalvars, evalints))
