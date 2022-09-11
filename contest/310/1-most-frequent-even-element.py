

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        res = None
        maxFreq = float("-inf")
        for key, freq in count.items():
            if key % 2 == 0 and freq >= maxFreq:
                if res == None or freq > maxFreq:
                    res = key
                    maxFreq = freq
                elif freq == maxFreq:
                    res = min(res, key)
        return res if res != None else -1
                
            
