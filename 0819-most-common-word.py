import re
import collections
class Solution(object):
    def mostCommonWord0(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        counter = collections.Counter(word.lower() for word in re.split('\W+', paragraph) if word)
        print(counter)
        print(counter.most_common())
        for word, _ in counter.most_common(): #sorted
            if word not in set(banned):
                return word

    def mostCommonWord1(self, paragraph, banned):
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(
            word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans

s = Solution()
print(s.mostCommonWord0("Bob hit a ball, the hit BALL flew far after it was hit.", "hit"))
print(s.mostCommonWord1("Bob hit a ball, the hit BALL flew far after it was hit.", "hit"))