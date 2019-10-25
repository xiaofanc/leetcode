import itertools
class Solution:
    def countAndSay0(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            temp = ""
            for digit, group in itertools.groupby(s):
                #print(digit, group)
                temp += ''.join(str(len(list(group))) + digit)
            s = temp
            print(s)
        return s

    def countAndSay1(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
            print(s)
        return s

    def countAndSay2(self, n):
        result = "1"
        for i in range(n-1):
          addtional = ""
          for digit, group in itertools.groupby(result):
            count = sum(1 for _ in group)
            addtional += str(count) + digit
          result = addtional
        return result
            
s=Solution()
print(s.countAndSay0(6))
print()
print(s.countAndSay1(6))
print()
print(s.countAndSay2(6))
print()