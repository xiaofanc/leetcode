"""
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.
"""

from collections import deque
class Solution:
	# TLE. Time: O(n^2 * m)
    def ladderLength(self, source: str, target: str, wordList: List[str]) -> int:
        queue = deque([(source, 1)])
        seen = set(source)
        while queue:
            word, depth = queue.popleft()
            if word == target:
                return depth
            for w2 in wordList:
                diff = 0
                for i in range(len(w2)):
                    if word[i] != w2[i]:
                        diff += 1
                if diff == 1 and w2 not in seen:
                    seen.add(w2)
                    queue.append((w2, depth+1))
        return 0

    # Time: O(n^2 * m), go over every edges for all possible patterns. Since the edges are pre-calculated, it will save some time.
    def ladderLength(self, source: str, target: str, wordList: List[str]) -> int:
        queue = deque([(source, 1)])
        seen = set(source)
        
        # get all patterns for wordList
        adj = defaultdict(set)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i+1:]
                adj[pattern].add(w)
        
        while queue:
            word, depth = queue.popleft()
            if word == target:
                return depth
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for nei in adj[pattern]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append((nei, depth+1))
        return 0

if __name__ == '__main__':
	s = Solution()
	print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # 5
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))  # 0


