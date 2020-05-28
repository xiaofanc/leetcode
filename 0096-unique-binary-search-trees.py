"""
dp[i] = dp[j] * dp[i-j-1]
dp[0] = 1
dp[1] = dp[0] * dp[0]
dp[2] = dp[0] * dp[1] + 
        dp[1] * dp[0]
dp[3] = dp[0] * dp[2] + 
        dp[1] * dp[1] + 
        dp[2] * dp[0]

dp[3]:
   1  
    \
     23
   
   2
  / \
 1   3 

   3
  /
 12
....
let dp[i]  = the number of unique BST given a sequence of length i
let F(i,n) = the number of unique BST, where the number i is served as the root of BST
Later we would see that dp[n] can be deducted from F(i, n) (i = [1,n]), 
which at the end, would recursively refers to dp[n].

First of all, following the idea in the section of intuition, we can see that the 
total number of unique BST dp[n], is the sum of BST F(i, n) enumerating each number 
i (1 <= i <= n) as a root. 
dp[n] = sum(F(i, n)) (1 <= i <= n)

Given a sequence 1 ... n, we pick a number i out of the sequence as the root, then 
the number of unique BST with the specified root defined as F(i, n), is the product 
of the number of BST for its left and right subtrees.
F(i, n) = dp[i-1] * dp[n-i] (1 <= i <= n)

base case: dp[0] = 1, dp[1] = 1
recursive relation: dp[i] = sum(dp[j] * dp[i-j-1]) & j -> [0,i-1]

"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        # base case: 
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[-1]

    def numTrees(self, n: int) -> int:
        dp = [1]
        for i in range(1, n+1):
            dp.append(sum(dp[j]*dp[i-j-1] for j in range(i)))
        return dp[-1]


                
                
if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(3) == 5)