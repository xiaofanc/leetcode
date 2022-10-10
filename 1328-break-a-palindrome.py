class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        arr = [char for char in palindrome]
        m = len(arr)//2
        for i in range(m):
            if arr[i] != 'a':
                arr[i] = 'a'
                return ''.join(arr)
        arr[len(arr)-1] = 'b'
        return ''.join(arr)

if __name__ == '__main__':
    s = Solution()
    print(s.breakPalindrome("abccba")) # "aaccba"
    print(s.breakPalindrome("aaaaa")) # "aaaab"
    print(s.breakPalindrome("a")) # ""
            
        
                    
                    

                