class Solution:
    # Time: O(n^2)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcounter = collections.Counter(p)
        ans = []
        for i in range(len(s)-len(p)+1):
            substring = s[i:i+len(p)] # O(n)
            scounter = collections.Counter(substring)
            if pcounter == scounter:
                ans.append(i)
        return ans

    # Time: O(n)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcounter = collections.Counter(p)
        scounter = collections.Counter()
        ns, np = len(s), len(p)
        if ns < np:
            return []
        ans = []
        
        for i in range(ns):
            scounter[s[i]] += 1
            if i >= np: # sliding window moves to the right one by one
                if scounter[s[i-np]] == 1:
                    del scounter[s[i-np]]
                else:
                    scounter[s[i-np]] -= 1
            if pcounter == scounter:
                ans.append(i-np+1)
                
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc")) # [0,6]


    