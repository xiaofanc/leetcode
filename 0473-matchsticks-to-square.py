"""
same as 698
split into 4 subsets with same sum

Time: O(4x2^n)
Space: O(n)
We have used an extra array of size N to mark the already used elements.
And the recursive tree makes at most N calls at one time, so the recursive stack also takes O(N) space.

"""

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4:
            return False
        target = sum(matchsticks) / 4
        # split matches to 4 subsets with target sum
        matchsticks.sort(reverse = True)
        used = [False] * len(matchsticks)
        
        def backtrack(i, cursum, count):
            if count == 3:
                return True
            if cursum == target:
                # find the next subset from beginning
                return backtrack(0, 0, count+1)
            if cursum > target:
                return False
            
            for j in range(i, len(matchsticks)):
                if used[j] or (j>0 and matchsticks[j] == matchsticks[j-1] and not used[j-1]):
                    continue
                used[j] = True
                if backtrack(j+1, cursum+matchsticks[j], count): return True
                used[j] = False
                
            return False
        
        return backtrack(0, 0, 0)

    # slow method
    # Time: O(4^N) because we have a total of N sticks and for each one of those matchsticks, we have 4 different possibilities for the subsets they might belong to or the side of the square they might be a part of.

    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4:
            return False
        target = sum(matchsticks) / 4
        # split matches to 4 subsets with target sum
        matchsticks.sort(reverse = True)
        sides = [0 for _ in range(4)]
        
        def backtrack(i):
            sums = [target for _ in range(4)]
            if sides == sums and i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        
        return backtrack(0)

if __name__ == '__main__':
	s = Solution()
	print(s.makesquare([1,1,2,2,2]))      # True




	
                