class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # if token is digit, save to stack
            # else if token is operator, pop out two numbers from stack and append the res
            # isnumeric() does not work for negative int
            if token in '+-*/':
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    res = num1 + num2
                elif token == "-":
                    res = num1 - num2
                elif token == "*":
                    res = num1 * num2
                else:
                    res = int(num1 / num2) # int(6/-132) = 0
                stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()
                
                
if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22