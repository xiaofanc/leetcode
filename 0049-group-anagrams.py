"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""

class Solution:
    # Time: O(mxnlogn), where n is the maximum length of a string
    # Space: O(mn)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list) # key is the tuple
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    # Time(mxnx26) -> Time(mxn)
    # Space: O(mn)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            arr = [0]*26
            for char in s:
                arr[ord(char)-ord('a')] += 1
            anagrams[tuple(arr)].append(s)
        # print("anagrams", anagrams)
        return anagrams.values()

if __name__ == '__main__':
	s = Solution()
	print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(s.groupAnagrams(["",""]))  # [["",""]]



    