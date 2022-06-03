"""
Greedy:
Start backwards
    - Is there a way to reach the goal (len(nums))? If nums[i] + i >= goal, then yes
    - Update the goal to be i

If the goal == 0, then return True

"""

class Solution:
    # greedy, Time: O(N)
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

    # recursion, Time: O(N^2)
    # top-down DP
    # check whether next possible position [index+1, furtherpos] can lead to the end
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        def helper(index):
            if index in dp:
                return dp[index]
            if index == len(nums)-1:
                return True
            furtherpos= min(index+nums[index], len(nums)-1)
            # try every possible step to see if can reach the end
            for i in range(furtherpos, index, -1):
                if helper(i):
                    dp[index] = True
                    return dp[index]
            dp[index] = False
            return dp[index]
        return helper(0)

    # bottom-up DP
    # check whether next possible position [i+1, furtherposition] can lead to the end
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums))
        dp[-1] = True
        for i in range(len(nums)-2, -1, -1):
            furtherposition = min(i+nums[i], len(nums)-1)
            for j in range(i+1, furtherposition+1):
                # there exists a position j which can make i reach the end
                if dp[j]:
                    dp[i] = True
                    break # break the j loop, continue the i loop
        return dp[0]

if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4])) # True
    print(s.canJump([3,2,1,0,4])) # False




