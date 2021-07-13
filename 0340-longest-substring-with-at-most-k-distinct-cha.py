"""
     [e c e b a]
left  0   2 3
right 0 1 2 3 4 5
k = 2
hashmap: {b:3, a:4}
max_len = 1, 2, 3

"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        if n*k == 0:
            return 0
        left = right = 0
        visited = dict()
        while right < n:
        	# hashmap to store the rightmost position for the character
            visited[s[right]] = right
            right += 1
            
            if len(visited) == k+1: 
                # remove the leftmost character from the hashmap
                # so that sliding window contains k distinct
                # characters only
                # [e c e b a], left will jump 0 -> 2 since 'c' is removed from hashmap
                del_idx = min(visited.values())
                del visited[s[del_idx]]
                left = del_idx + 1
                
            res = max(res, right - left)
        return res

    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values()) # c:1
                del d[s[low]]
                low += 1    # 2
            ret = max(i - low + 1, ret)
        return ret

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        if n*k == 0:
            return 0
        left = right = 0
        visited = {}
        while right < n:
            visited[s[right]] = visited.get(s[right], 0) + 1
            if len(visited) > k:
                # remove leftmost character
                # print(left, s[left])
                visited[s[left]] -= 1
                if visited[s[left]] == 0:
                    del visited[s[left]]
                left += 1
                
            res = max(res, right - left + 1)
            right += 1
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.lengthOfLongestSubstringKDistinct("abaccc", 2)) # 4
	print(s.lengthOfLongestSubstringKDistinct("eceba", 2)) # 3



