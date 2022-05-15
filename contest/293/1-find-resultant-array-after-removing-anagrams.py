"""
Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
Explanation:
One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","baba","cd","cd"].
- Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
  Now words = ["abba","cd","cd"].
- Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","cd"].
We can no longer perform any operations, so ["abba","cd"] is the final answer.

"""
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def anagrams(s, t):
            sc = collections.Counter(s)
            tc = collections.Counter(t)
            return sc == tc
        res = []
        for i in range(len(words)-1, -1, -1):
            if i >= 1 and anagrams(words[i], words[i-1]):
                continue
            else:
                res.append(words[i])
        return res[::-1]
            
if __name__ == '__main__':
    s = Solution()
    print(s.removeAnagrams(["a","b","c","d","e"])) # ["a","b","c","d","e"]
    print(s.removeAnagrams(["abba","baba","bbaa","cd","cd"])) # ["abba","cd"]
