"""
Given an encoded string, return its decoded string.
Using stack to store the prevstr and nums before '['
"""
class Solution: # Time: O(n)
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
                # stack ['', 3, 'a', 2]
                num = stack.pop()
                prevstr = stack.pop()         # prevstr can be empty string
                curstr = prevstr + num*curstr # aaa + 2*bc
            elif c.isdigit():
                nums = nums*10 + int(c) # for numbers > 9
            else: # .isalpha()
                curstr += c
        return curstr

    def decodeString(self, s: str) -> str:
        curstr = ''
        stack = [] # store the prevstr and nums before '['
        nums = 0
        # "3[a]2[bc]"
        for c in s:
            if c == '[':
                stack.append(curstr) # ''  'aaa'
                stack.append(nums)   # 3   2
                nums = 0
                curstr = ''
            elif c == ']':
                num = stack.pop()   # 3   2
                prevstr = stack.pop()  # ''  'aaa'
                curstr = prevstr + num*curstr # 'aaa'  'aaabcbc'
            elif c.isdigit():
                nums = nums*10 + int(c) # 2
            else:
                curstr += c  # 'a'  'bc'
        return curstr
        
                
if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))  # "aaabcbc"
    print(s.decodeString("abc3[cd]xyz2[a]")) # "abccdcdcdxyzaa"
    print(s.decodeString("abc3[cd3[s]]xyz"))  # "abccdssscdssscdsssxyz"