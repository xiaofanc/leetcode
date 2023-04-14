"""
You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

- Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
- Add the value of the chosen integer to score.
- Mark the chosen element and its two adjacent elements if they exist.
- Repeat until all the array elements are marked.
- Return the score you get after applying the above algorithm.
"""
class Solution:
    def findScore(self, nums: List[int]) -> int:
        idxes = [(n, i) for i, n in enumerate(nums)]
        marked = set()
        res = 0
        for n, i in sorted(idxes):
            if i not in marked:
                res += n
                marked.add(i)
                marked.add(i-1)
                marked.add(i+1)
        return res
            
