"""
How to deal with priority in (6/2+8)?
calculate 6/2 before add +8

"""

"""
How to deal with priority in (6/2+8)?
calculate 6/2 before add +8

"""

class Solution:
    def calculate(self, s: str) -> int:
        
        def operations(oper, b, a):
            if oper == "+":
                return a+b
            elif oper == "-":
                return a-b
            elif oper == "*":
                return a*b
            else:
                return a//b
    
        def predence(cur, prev):
            # return false if no need to pre-calculate in the stack
            if prev in ("(", ")"):
                return False
            if cur in ("*", "/") and prev in ("+", "-"):
                return False
            return True
        
        operators = []
        nums = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = int(s[i])
                while i < len(s)-1 and s[i+1].isdigit():
                    num = num * 10 + int(s[i+1])
                nums.append(num)
            elif s[i] == "(":
                operators.append(s[i])
            elif s[i] == ")":
                while operators[-1] != "(":
                    nums.append(operations(operators.pop(), nums.pop(), nums.pop()))
                operators.pop() # pop "("
            else:
                if operators and predence(s[i], operators[-1]):
                    nums.append(operations(operators.pop(), nums.pop(), nums.pop()))
                operators.append(s[i])
        while operators:
            num = operations(operators.pop(), nums.pop(), nums.pop())
            nums.append(num)
        return nums[-1]

class Solution:
    def calculate(self, s: str) -> int:

        s = list(s)    

        def helper(s):        
            stack = []
            sign = "+"
            num = 0
            while len(s) > 0:
                c = s.pop(0)
                if c.isdigit():
                    num = num*10 + int(c)
                    
                # 如果是括号，使用递归先计算出括号里的
                if c == "(":
                    num = helper(s)
                
                if (not c.isdigit() and c != " ") or len(s) == 0:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "*":
                        stack[-1] = stack[-1]*num
                    elif sign == "/":
                        stack[-1] = int(stack[-1]/float(num))
                    print("stack ->", stack, c, sign)

                    num = 0
                    sign = c

                # 遇到右括号，返回递归结果
                if c == ")":
                    break
            return sum(stack)
        return helper(s)

if __name__ == '__main__':
	s = Solution()
	print(s.calculate("2*(5+5*2)/3+(6/2+8)")) # 21




