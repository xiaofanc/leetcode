class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2+1):
            if len(s) % i == 0:
                pattern = s[:i] * (len(s)//i)
                if pattern == s:
                    return True
        return False

#The maximum length of a "repeated" substring that you could get from a string would be half it's length
#For example, s = "abcdabcd", "abcd" of len = 4, is the repeated substring.
#You cannot have a substring >(len(s)/2), that can be repeated.
#
#So, when ss = s + s , we will have atleast 4 parts of "repeated substring" in ss.
#(s+s)[1:-1], With this we are removing 1st char and last char => Out of 4 parts of repeated substring, 2 part will be gone (they will no longer have the same substring).
#ss.find(s) != -1, But still we have 2 parts out of which we can make s. And that's how ss should have s, if s has repeated substring.

    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        ss = (s+s)[1:-1]
        return ss.find(s) != -1
        # return s in (2*s)[1:-1]