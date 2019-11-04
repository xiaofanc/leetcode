class Solution:
    def defangIPaddr(self, address: str) -> str:
        #return '[.]'.join(address.split('.'))
        return address.replace('.','[.]')


if __name__ == '__main__':
	s = Solution()
	print(s.defangIPaddr("255.100.50.0"))