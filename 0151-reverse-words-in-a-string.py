class Solution:
    # Time: O(n)
    def reverseWords(self, s: str) -> str:
        chars = s.split(" ")
        chars = [char for char in chars if char != ""]
        res = ""
        for char in chars[::-1]:
            res += char + " "
        return res[:-1]

        # return " ".join(reversed(s.split()))

    def reverseWords(self, s: str) -> str:
        s = s.strip() # remove all the leading and trailing spaces from a string
        def reverse(word):
            l, r = 0, len(word)-1
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            return word
        # reverse s
        slist = reverse(list(s))
        output = []
        l, r = 0, 0
        while r < len(slist):
            if slist[r] != " ":
                r += 1
            else:
                output.append(''.join(reverse(slist[l:r])))
                while slist[r] == " ":
                    r += 1
                l = r
        output.append(''.join(reverse(slist[l:r])))
        return " ".join(output)

s = Solution()
print(s.reverseWords("the sky is     blue")) # "blue is sky the"