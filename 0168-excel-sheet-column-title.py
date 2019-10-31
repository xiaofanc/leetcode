class Solution:
    
    def convertToTitle0(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)
    
    def convertToTitle1(self, n):
        chars = {i:c for i,c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        ans = []
        while n>0:
            n -= 1
            n,res = divmod(n,26)
            ans.append(res)
            print(n,res)
        ans = [chars[a] for a in reversed(ans)]
        return ''.join(ans)

    def convertToTitle2(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        distance = ord('A') 

        while n > 0:
            y = (n-1) % 26
            n = (n-1) // 26
            print(n,y,y+distance,chr(y+distance))
            s = chr(y+distance)
            result = ''.join((s, result))

        return result
        
if __name__ == '__main__':
	s=s = Solution()
	print(s.convertToTitle0(26))
	print()
	print(s.convertToTitle1(26))
	print()
	print(s.convertToTitle1(27))
	print()
	print(s.convertToTitle0(701))
	print()
	print(s.convertToTitle1(701))
	print()
	print(s.convertToTitle2(701))