"""
Given two integers num and k, consider a set of positive integers with the following properties:

The units digit of each integer is k.
The sum of the integers is num.

Input: num = 58, k = 9
Output: 2
Explanation:
One valid set is [9,49], as the sum is 58 and each integer has a units digit of 9.
Another valid set is [19,39].
It can be shown that 2 is the minimum possible size of a valid set.

methodology:
candidates: [49,39,29,19,9], select min numbers from candidates that sum up to num..
- start from the largest candidate, if found a combination, then return
- since starting from the largest, we will get min num once we find one combination
edge case: 
- if num == 0: return 0
- if no such combination can be found: return -1
- if num < k: return -1
early stop:
The unit digits for the sum can be ?
If the unit digits of n is not in the possible situation: return -1

Math solution:
All numbers must have k as the unit digit
So A1 + A2 + ... + An = n*k + 10*(a1 + a2 + .. + an) = sum
Just find the minimum number satisfying the condition (n*k) % 10 == sum % 10
"""

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if num < k:
            return -1

        # early stop
        units = set()
        for i in range(1, 11):
            units.add(k * i % 10)
        if num % 10 not in units:
            return -1
        
        # get the largest number that ends with k
        start = num // 10 * 10 + k
        res = float("inf")
        
        def combination(n, comb):
            nonlocal res, units
            if sum(comb) == num:
                res = min(res, len(comb))  # once we find one comb, then that's the min nums
                return 1
            if sum(comb) > num:
                return 
            # early stop
            if n % 10 not in units:
                return -1
            ans = -1
            for i in range(start, k-1, -10):
                comb.append(i)
                ans = combination(i, comb)
                if ans == -1: return -1   # early stop
                if ans == 1: return 1     # stop when finding one combination
                comb.pop()
            return ans
        if combination(start, []) == -1 or res == float("inf"): return -1
        return res
    
    # A1 + A2 + ... + An = n*k + 10*(a1 + a2 + .. + an) = sum
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for i in range(1, 11):
            if (k * i) % 10 == num % 10 and k * i <= num:
                return i
        return -1

if __name__ == '__main__':
	s = Solution()
	print(s.minimumNumbers(37, 2)) # -1
	print(s.minimumNumbers(0, 2))  # 0
	print(s.minimumNumbers(10, 1))  # 10
	print(s.minimumNumbers(4, 0))  # -1





        
        
        