"""
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.

It is like placing each element in k different subsets.
So we assign each and every bag of cookies to different subsets using backtracking and if all are distributed, we check for the maximum element in that case, and update our ans according to it.
let n = size of given array, as for each element we have k subset choices and there are total of n elements, so Time complexity : O(k^n)

Get the minmax for k subsets.
"""

class Solution:
    # incorrect logic
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        import math
        target = math.ceil(sum(cookies) / k)
        cookies.sort()
        n = len(cookies)
        res = []
        def subset(start, comb):
            if sum(comb) >= target:
                res.append(sum(comb))
                return
            for j in range(start, n):
                comb.append(cookies[j])
                subset(j+1, comb)
                comb.pop()
        subset(0, [])
        return min(res)


    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # split cookies into k subsets and find the minmax
        if len(cookies) <= k:
            return max(cookies)
        ans = float("inf")
        fair = [0]*k
        def backtracking(i):
            nonlocal ans
            if i == len(cookies):
                ans = min(ans, max(fair))
                return
            # Bounding condition to stop a branch if unfairness already exceeds current optimal soltution
            if max(fair) > ans:
                return
            for j in range(k):
                fair[j] += cookies[i]
                backtracking(i+1)
                fair[j] -= cookies[i]
        backtracking(0)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.distributeCookies([8,15,10,20,8], 2))  # 31
    print(s.distributeCookies([6,1,3,2,2,4,1,2], 3))  # 7



