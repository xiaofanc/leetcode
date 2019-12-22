# explaination:
# https://leetcode.com/problems/paint-fence/discuss/178010/The-only-solution-you-need-to-read

#// sum of all possible ways where last 2 posts are different color and same color
#num_ways(i) = num_ways_diff(i) + num_ways_same(i); 

#// all possible ways so far multiplied by k-1 colors since we can't paint the same color.
#num_ways_diff(i) = num_ways(i-1) * (k-1);

#// if last 2 posts (i-1 and i-2) are the same color then we can't paint the same therefore use num_ways_diff(i-1) instead of num_ways(i-1)
#// multiply by 1 because there is only single color to paint with
#num_ways_same(i) = num_ways_diff(i-1) * 1; 

#// just substitute num_ways_diff(i-1) using i = i-1
#num_ways_same(i) = num_ways(i-2) * (k-1) * 1;  

#// so total becomes
#num_ways(i) = num_ways(i-2) * (k-1) + num_ways(i-1) * (k-1);

class Solution:
    def numWays(self, n: int, k: int) -> int:
        paint = [0, k, k*k]
        while len(paint) <= n:
            paint.append(sum(paint[-2:])*(k-1))
        return paint[n]

#https://leetcode.com/problems/paint-fence/discuss/71150/Python-solution-with-explanation
    def numWays(self, n: int, k: int) -> int:
    	if n == 0:
    		return 0
    	if n == 1:
    		return k
    	# n == 2
    	same, diff = k, k*(k-1)
    	for i in range(3, n+1):
    		same, diff = diff, (same+diff)*(k-1)
    	return same + diff

   if __name__ == '__main__':
   	s = Solution()
   	print(s.numWays(3,2))

