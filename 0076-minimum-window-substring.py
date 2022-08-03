"""
We start with two pointers, left and right initially pointing to the first element of the string S.

We use the right pointer to expand the window until we get a desirable window i.e. a window that contains all of the characters of T.

Once we have a window with all the characters, we can move the left pointer ahead one by one. If the window is still valid we keep on updating the minimum window size.

If the window is not valid any more, we repeat step2 onwards.

dict_t = {'a':1, 'b':1, 'c':1}, required = 3
window_counts = {'a':1, 'b':2, 'c':1}, formed = 3
valid window, update res

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
                


    def minWindow(s, t):
        target = collections.Counter(t)
        conditions = 0
        window = {}
        length = len(s)
        res = ""
        l, r = 0, 0
        while r < len(s):
            # when the window is not found, move right pointer + 1
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in target and window[s[r]] == target[s[r]]:
                conditions += 1
            # move the left pointer until condition does not meet, get the min length
            while conditions == len(target):
                if r-l+1 < length:
                    res = s[l:r+1]
                    length = r-l+1
                window[s[l]] -= 1
                # window[s[l]] != target[s[l]] does not work 
                # window[s[l]] can be > target[s[l]], but it still meet the condition
                if s[l] in target and window[s[l]] < target[s[l]]:
                    conditions -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            r += 1
        return res
                
if __name__ == '__main__':
	s = Solution()
	print(s.minWindow("ADOBECODEBANC", "ABC")) # "BANC"
    print(s.minWindow("a", "b")) # ""
    print(s.minWindow("a", "ab")) # ""





	