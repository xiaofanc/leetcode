"""
A string is beautiful if:

It consists of the first k letters of the English lowercase alphabet.
It does not contain any substring of length 2 or more which is a palindrome.

"abdc", 4 -> "acba"   "aca." does not work

s is beatiful, so it does not contain any substring of length 2 or more which is a palindrome.
The key point is that the valid string is just a string that satisfy s[i] != s[i - 1] && s[i] != s[i - 2] for all indices i.
First, from right to left, find which index's character can be increased. Note, altough I use a loop here, the number of iterations is at most 3. Since we only need to "+1" when s[i] == s[i - 1] or s[i] == s[i - 2]. And we need to make sure s[i] <= 'a' + k - 1.    
Second, If s[i] can be increased into c, then we just make the characters from index (i + 1) as small as possible. Note s was beatiful before and if we can increase s[i], the remaining characters will always have solution. (Since it has s[x] != s[x - 1] && s[x] != s[x - 2] before, meaning we should have at least 3 candidate characters and for each position we must have a way to select a new character that is different from the previous 2).
"""


class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        A = [ord(c)-ord('a') for c in s]
        i = n-1
        A[i] += 1
        # find which index can be increased
        while i >= 0:
            if A[i] >= k:
                i -= 1
            elif A[i] not in A[max(i-2,0):i]: # found
                break
            A[i] += 1
        if i < 0:
            return ''
        # A[:i+1] is beatiful, make A[i+1:] as small as possible
        # There are only 3 possible candidates for each position
        for j in range(i+1, n):
            A[j] = min({0,1,2}-set(A[max(j-2,0):j]))
        return ''.join(chr(ord('a')+a) for a in A)



        
        
                
                
        
        