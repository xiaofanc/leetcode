"""
We start with two pointers, left and right initially pointing to the first element of the string S.

We use the right pointer to expand the window until we get a desirable window i.e. a window that contains all of the characters of T.

Once we have a window with all the characters, we can move the left pointer ahead one by one. If the window is still a desirable one we keep on updating the minimum window size.

If the window is not desirable any more, we repeat step2 onwards.

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""    
        # count for each unique characters
        dict_t = collections.Counter(t)
        
        # required number of unique characters in t
        required = len(dict_t)
        
        # dictionary which keeps a count of all the unique characters in the current window
        window_counts = {}
        
        # Counter for the current window
        formed = 0
        
        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None
        
        # start by pointing to the first element of the string
        l = r = 0
        # use right to expand the window until we get a desirable window with t
        while r < len(s):
            # add one character from the right to the window
            c = s[r]
            window_counts[c] = window_counts.get(c, 0) + 1
            if c in dict_t and window_counts[c] == dict_t[c]:
                formed += 1
            # try and contract the window it ceases to be 'desirable'
            # while l <= r and formed == required:
            while formed == required:
                c = s[l]
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)
                # the current left pointer is removed from the current window
                window_counts[c] -= 1
                if c in dict_t and window_counts[c] < dict_t[c]:
                    formed -= 1
                # move left to next
                l += 1
            # keep expanding the window once we are done contracting
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
                
                
if __name__ == '__main__':
	s = Solution()
	print(s.minWindow("ADOBECODEBANC", "ABC")) # "BANC"
    print(s.minWindow("a", "b")) # ""





	