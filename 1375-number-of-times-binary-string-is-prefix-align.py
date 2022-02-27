"""
right is the number of the right most lighted bulb.
Iterate the input light A, update right = max(right, A[i]).
Now we have lighted up i + 1 bulbs if right == i + 1.
it means that all the previous bulbs (to the left) are turned on too.
Then we increment res.

       [3,2,4,1,5]
right =[3,3,4,4,5]
i     =[1,2,3,4,5]   # number of bulb on

"""

class Solution:
	# Time out
    def numTimesAllBlue(self, flips: List[int]) -> int:
        if not flips:
            return 0
        string = ["0"] * len(flips)
        count = 0
        for i in range(len(flips)):
            string[flips[i]-1] = "1"
            if "".join(string[:i+1]) == "1"*(i+1):
                count += 1
        return count

    def numTimesAllBlue(self, A):
        right = res = 0
        for i, a in enumerate(A, 1): # start from 1
            right = max(right, a)  # right most bulb
            res += right == i
        return res

    def numTimesAllBlue(self, light: List[int]) -> int:
        res = hi = on = 0
        for l in light:
            on += 1
            if l>hi:
                hi = l
            if on==hi:
                res+=1
        return res

    def numTimesAllBlue(self, light: List[int]) -> int:
        return sum(i == m for i,m in enumerate(accumulate(light, max), 1))
        
if __name__ == '__main__':
	s = Solution()
	print(s.numTimesAllBlue([3,2,4,1,5])) #2



