"""
constraint: 
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split(" ")])

    def reverseWords(self, s: str) -> str:
        def helper(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        arr = [c for c in s]
        
        l = r = 0
        while r < len(s):
            if s[r] != " ":
                r += 1
            else:
                helper(l, r-1)
                r += 1 # single space
                l = r
        helper(l, r-1)
        return "".join(arr)

    def reverseWords(self, s: str) -> str: # multiple spaces work
        res = ""
        cur = ""
        for char in s:
            if char == " ":
                res += cur + " "
                cur = ""
            else:
                cur = char + cur
        res += cur
        return res

    def reverseWords(self, s: str) -> str:  # single space
        start = 0
        arr = [c for c in s]
        for i in range(len(arr)+1):
            if i == len(arr) or arr[i] == " ":
                end = i-1
                while start < end:
                    arr[start], arr[end] = arr[end], arr[start]
                    start += 1
                    end -= 1
                start = i+1
        return "".join(arr)

s=Solution()
print(s.reverseWords("Let's take LeetCode contest"))

