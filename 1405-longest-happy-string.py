"""
In this solution, each loop adds a group of 2~3 characters. A group starts with a 'fence' of 1~2 characters in its front and ends with a single 'wedge' character. The wedge character divides current group from next group.
Using == to denote the fence and | to denote the wedge, the happy string should resemble the pattern ==| ==| ==|...==| ==.
For example, when a = 1, b = 1, c = 7，output consists of groups cca ccb cc
Decide the fence and wedge characters to be placed in current group.

a. We select the character with the highest remaining count to be the fence, and character with the second highest to be the wedge, thus allowing us to create as many groups as possible.
In order to make the string as long as possible, for every two fences, we put one wedge.
b. Every time we put a wedge, we need to check if wedge is the same as previous two characters.
"""


class Solution:
	# time for heappush/heappop -> O(logn)
	# Time: O(klogn)
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = []
        maxheap = []
        for count, token in ((-a, "a"), (-b, "b"), (-c, "c")):
            if count: heapq.heappush(maxheap, (count, token))
        
        while maxheap:
            first, token1 = heapq.heappop(maxheap)
            if len(s) >= 2 and (s[-1] == s[-2] == token1):
                # get other tokens
                if not maxheap:
                    return "".join(s)
                second, token2 = heapq.heappop(maxheap)
                # print("token2:", token2)
                s.append(token2)
                second += 1
                if second:
                    heapq.heappush(maxheap, (second, token2))
                # put back the first token
                heapq.heappush(maxheap, (first, token1))
                # print(s)
                # print(maxheap)
            else:
                s.append(token1)
                first += 1
                if first:
                    heapq.heappush(maxheap, (first, token1))
                print(s)
                print(maxheap)
            
        return "".join(s)


    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = []
        maxheap = []
        for count, token in ((-a, "a"), (-b, "b"), (-c, "c")):
            if count: heapq.heappush(maxheap, (count, token))
        
        while maxheap:
            count, token = heapq.heappop(maxheap)
            if len(s) >= 2 and (s[-1] == s[-2] == token):
                # get other tokens
                if not maxheap:
                    return "".join(s)
                # put back the first token and pop the smallest item from the heap
                count, token = heapq.heapreplace(maxheap, (count, token))
            s.append(token)
            count += 1
            if count:
                heapq.heappush(maxheap, (count, token))
            
        return "".join(s)
                    

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for count, token in (-a, 'a'), (-b, 'b'), (-c, 'c'):
            if count: heapq.heappush(max_heap, (count, token))
        result = []
        while max_heap:
            count, token = heapq.heappop(max_heap)
            if len(result) > 1 and result[-2] == result[-1] == token:
                if not max_heap: break
                count, token = heapq.heapreplace(max_heap, (count, token))
            result.append(token)
            if count + 1: heapq.heappush(max_heap, (count + 1, token))
        return ''.join(result)

s = Solution()
print(s.longestDiverseString(7, 1, 0))   # "aabaa"



