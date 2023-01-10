class Solution:
    """
    Time: O(N^3)
    There are O(N^2) states corresponding to entries of dp,
    and we do an average of O(N) work on each state.
    """
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def backtrack(i, left):
            if (i, left) in memo:
                return memo[(i, left)]
            if i == len(s):
                if left == 0:
                    return True
                else:
                    return False

            if left < 0:
                return False

            if s[i] == "(":
                memo[(i, left)] = backtrack(i+1, left+1)
                return memo[(i, left)]
            elif s[i] == ")":
                memo[(i, left)] = backtrack(i+1, left-1)
                return memo[(i, left)]
            else:
                memo[(i, left)] = backtrack(i+1, left+1) or backtrack(i+1, left-1) or backtrack(i+1, left)
                return memo[(i, left)]

        return backtrack(0, 0)

    # Greedy: O(N)
    def checkValidString(self, s: str) -> bool:
        # Let lo, hi respectively be the smallest and largest possible number of open left brackets after processing the current character in the string.
        lo, hi = 0, 0
        for c in s:
            # treat * as )
            lo += 1 if c == "(" else -1
            # treat * as (
            hi += 1 if c != ")" else -1
            # if hi < 0, treat all * as ( is not enough
            if hi < 0:
                return False
            # there is always a way to make the substring valid if hi >= 0
            lo = max(lo, 0)

        # if lo > 0, too many (
        # if lo < 0, there is always a way to make the string valid since hi >= 0
        return lo == 0



