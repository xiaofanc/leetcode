"""
sliding window:
We use HashSet to store the characters in current window [i,j)
Then we slide the index j to the right
If it is not in the HashSet, we slide j further. 
Doing so until s[j] is already in the HashSet. 
At this point, we found the maximum size of substrings without duplicate characters start with index i


"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, lo, hi = 0, 0, 0
        charidx = {}
        for hi in range(len(s)):
            shi = s[hi]
            if shi in charidx:
                lo = max(lo, charidx[shi])
            ans = max(ans, hi-lo+1)
            charidx[shi] = hi+1
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        ans = 0
        chars = dict()
        
        for high in range(len(s)):
            shi = s[high]
            if shi in chars:
                low = max(chars[shi]+1, low)
            chars[shi] = high
            ans = max(ans, high-low+1)
        return ans
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, lo, hi = 0, 0, 0
        charidx = {}
        for hi in range(len(s)):
            if s[hi] in charidx and lo <= charidx[s[hi]]: # shi show again
                lo = charidx[s[hi]] + 1  # cut off the previous occurrence 
            else:
                ans = max(ans, hi-lo+1)
            charidx[s[hi]] = hi
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            # print('r', r)
            chars[ord(r)] += 1
            while chars[ord(r)] > 1: # how to move the left pointer
                l = s[left]
                # print("l--->", l)
                # "pwp" - left moves from first 'p' to 'w'; "pww" - left moves from 'p' to second 'w'
                chars[ord(l)] -= 1   
                left += 1
            # print('left', left)
            # print('right', right)
            res = max(res, right - left + 1)

            right += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb") == 3)