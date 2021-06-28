class Solution:

    # time: O(2n+nlogn), space: O(n)
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        dct = {}
        news = ""
        for i in range(len(indices)):
            dct[indices[i]] = s[i]
        
        for k in sorted(dct.keys()):
            news += dct[k]
        
        return news

    def restoreString(self, s: str, indices: List[int]) -> str:
        
        return ''.join(c for _, c in sorted(zip(indices, s)))

    
    # time: O(n), space: O(n)
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        res = [0]*len(s)
        
        for i in range(len(s)):
            res[indices[i]] = s[i]
        
        return "".join(res)    
            
if __name__ == '__main__':
    s = Solution()
    print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3]))