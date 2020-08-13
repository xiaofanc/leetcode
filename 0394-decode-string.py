"""
Given an encoded string, return its decoded string.
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curstr = ''
        nums = 0
        for c in s:
            #print('nums=%s, curstr=%s, stack=%s' % (nums, curstr, stack))
            if c == "[":
                stack.append(curstr) # store previous str
                stack.append(nums)
                nums = 0
                curstr = ''
            elif c == ']':
                num = stack.pop()
                prevstr = stack.pop()
                curstr = prevstr + num*curstr # aaa + 2*bc
            elif c.isdigit():
                nums = nums*10 + int(c) # for numbers > 9
            else: # .isalpha()
                curstr += c
        return curstr
                
                
if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))  # "aaabcbc"
    print(s.decodeString("abc3[cd]xyz2[a]")) # "abccdcdcdxyzaa"
    print(s.decodeString("abc3[cd3[s]]xyz"))  # "abccdssscdssscdsssxyz"