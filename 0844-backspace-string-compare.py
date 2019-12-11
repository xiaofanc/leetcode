class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(a):
            newa = []
            for i in range(len(a)):
                if a[i] != "#":
                    newa.append(a[i])
                elif newa:
                    newa.pop()
            return newa
        return helper(S) == helper(T)
        
                
if __name__ == '__main__':
    s = Solution()
    print(s.backspaceCompare("a#c", "b"))