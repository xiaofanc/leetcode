"""
Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.
"""

class Solution:
    # Time: O(2^n) - number of node in the tree
    # Space: O(2^n)
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        if n == 1: # no consectutive digits, all single digit is valid no matter k
            return[i for i in range(10)]
        
        ans = []
        def DFS(n, num):
            """
            add n remaining digits after num, if diff = 2, DFS(1, 13)
            Starting from the second highest position, we could have at most 2 candidates.
            -> 131, 135
            """
            if n == 0:
                return ans.append(num)
            # Otherwise, remaining digits to be added to the current number
            tail = num % 10
            # using set() to avoid duplicates when K == 0
            next_digits = set([tail+k, tail-k])
            for digit in next_digits:
                if 0 <= digit < 10:
                    new_num = num * 10 + digit
                    DFS(n-1, new_num)
        
        # the first digit can be [1, 9], left n-1 digits
        for i in range(1, 10):
            DFS(n-1, i)
        return ans

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        if n == 1: # no consectutive digits
            return[i for i in range(10)]
        
        queue = [i for i in range(1, 10)] # first digit
        
        for level in range(n-1): # remain n-1 digits
            next_queue = []
            for num in queue:
                tail = num % 10
                next_digits = set([tail+k, tail-k])
                for digit in next_digits:
                    if 0 <= digit < 10:
                        new_num = num * 10 + digit
                        next_queue.append(new_num)
            queue = next_queue
        return queue
        
if __name__ == '__main__':
    s = Solution()
    print(s.numsSameConsecDiff(3, 7)) # [181,292,707,818,929]      
    print(s.numsSameConsecDiff(3, 2)) # [131, 135, 246, 242, 202, 313, 353, 357...]   



