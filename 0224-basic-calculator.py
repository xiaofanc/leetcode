"""

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

"""

class Solution:
    # one stack stores operator and its priority
    # one stack stores operand
    # remember the priority of +/-
    # add the priority by 1 if '(', and reduce the priority by 1 if ')'
    # if the priority of +/- less than the priority of the last operator on the stack, then start pop until empty or priority larger than the last operator on the stack
    # push back the result to stack

    def do_math(self, n1, n2, operator):
        res = 0
        if operator == "+":
            res = n1 + n2   
        else:
            res = n1 - n2
        return res

    def calculate(self, s: str) -> int:
        operator_stack = []
        operand_stack = []
        priority = 0
        nums = 0
        for c in s:
            if c.isnumeric():
                nums = nums*10 + int(c)
            elif c == '(':
                priority += 1
            elif c in '+-':
                operand_stack.append(nums)
                nums = 0
                while operator_stack != [] and operator_stack[-1][1] >= priority:
                    nums2 = operand_stack.pop()
                    nums1 = operand_stack.pop()
                    operator = operator_stack[-1][0]
                    operator_stack.pop()
                    #print(nums1, nums2, operator[0])
                    res = self.do_math(nums1, nums2, operator)
                    operand_stack.append(res)
                operator_stack.append((c, priority))
            elif c == ')':
                priority -= 1
        # the last number does not have +/- behind
        if nums != 0: 
            operand_stack.append(nums)
        # print(operand_stack, operator_stack)
        # when there is anything left on stack
        while operand_stack != [] and len(operand_stack) >= 2:
            # print(operand_stack, operator_stack)
            nums2 = operand_stack.pop()
            nums1 = operand_stack.pop()
            operator = operator_stack[-1][0]
            operator_stack.pop()
            #print(nums1, nums2, operator)
            res = self.do_math(nums1, nums2, operator)
            operand_stack.append(res) 
        # only an int in the string
        if operator_stack == [] and operand_stack == []: return int(s)

        return operand_stack[0]

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0
        sign = 1 # 1 mean positive
        for ch in s:
            print("ch: %s, sign: %s, operand: %s, res: %s, stack: %s" % (ch, sign, operand, res, stack))
            if ch.isdigit():
                operand = operand*10 + int(ch) # more than one digit
            elif ch == "+":
                res += sign*operand
                sign = 1
                operand = 0  # reset operand
            elif ch == "-":
                res += sign*operand # previous sign
                sign = -1
                operand = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ')':
                res += sign*operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0
        return res + sign*operand
                             

            
if __name__ == '__main__':
    s = Solution()
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
            
