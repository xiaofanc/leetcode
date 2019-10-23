class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        num1, num2 = list(num1), list(num2)
        while len(num1) > 0 or len(num2) > 0:
            n1 = ord(num1.pop())-ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop())-ord('0') if len(num2) > 0 else 0
            temp = n1 + n2 + carry
            res.append(temp % 10)
            carry = temp // 10
        if carry: res.append(carry)
        return ''.join([str(i) for i in res[::-1]])

s=Solution()
print(s.addStrings("12234","25933"))