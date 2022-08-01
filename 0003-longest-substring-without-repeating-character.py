"""
sliding window:
Solution 1:
Use hashset to store the char visited
If the right char is in the hashset: move the left pointer until char is not in the hashset
Update the res

Solution 2:
We use Hashmap to store the characters index in current window [i,j)
Then we slide the index j to the right
    - if it is not in the Hashmap, we slide j further
    - if it is in the Hashmap, update l = max(l, hashMap[char] + 1)
      --> move the left pointer to the previous index of repeated char + 1, do not move back
      --> why not l += 1? not enough. i.e. s = "pwwkew"
      --> why not l = hashMap[char] + 1? keep the left boundary of the sliding window. i.e. s = "tmmzuxt"
- update the hashmap and res along the way

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use dictionary to keep track of the number of unique chars in the sliding window
        # when right pointer meets duplicate char c
        # left pointer needs to move to the previous c + 1 position
        # so that the sliding window [l, r] only include unique chars
        count = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            while count[s[r]] > 1:
                # move the left pointer
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l = res = 0
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            res = max(res, r-l+1)
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        # hashmap to store the index of char
        hashMap = {}
        res = l = 0
        for r in range(len(s)):
            char = s[r]
            if char not in hashMap:
                hashMap[char] = r
            else:
                l = max(l, hashMap[char] + 1)
                hashMap[char] = r
            # print("l,r", l, r)
            res = max(res, r-l+1)
        return res

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
    print(s.lengthOfLongestSubstring("pwwkew") == 3)  # l should not only += 1
    print(s.lengthOfLongestSubstring("tmmzuxt") == 5) # l should not move back




