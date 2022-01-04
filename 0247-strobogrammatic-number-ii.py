"""
n == 1: [0,1,8]
n == 2: [11,88,69,96]
n == 3: insert [0,1,8] to the middle of the solution n=2
n == 4: insert [11,88,69,96,00] to the middle of the solution n=2 -> [1881...]
n == 5: insert [0,1,8] to the middle of the solution n=4
n == 6: insert [11,88,69,96,00] to the middle of the solution n=4 -> [181181...]

"""

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        oddmid = ["0", "1", "8"]
        evenmid = ["00", "11", "88", "69", "96"]
        if n == 1:
            return oddmid
        if n == 2:
            return evenmid[1:] # "00" does not count when n = 2
        if n % 2 == 1:
            prev, mid = self.findStrobogrammatic(n-1), oddmid
        else:
            prev, mid = self.findStrobogrammatic(n-2), evenmid
        premid = (n-1)//2
        return [p[:premid] + m + p[premid:] for p in prev for m in mid]

if __name__ == '__main__':
	s = Solution()
	print(s.findStrobogrammatic(3)) # ["101","111","181","808","818","888","609","619","689","906","916","986"]




	