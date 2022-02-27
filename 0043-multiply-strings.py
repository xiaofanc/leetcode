"""
Sum the products from all pairs of digits
when we multiply two digits, one from the first number and one from the second number, then their product will have some zeros appended at the end. The number of zeros depends on the place of each digit.
As an example, when we multiply two tens place digits, two zeros are appended at the end of the multiplication result, and the result will be added at the hundreds place in the final answer. 
Each time we will get a 2-digit result with some zeros after it. Since we know how many zeros will follow the product of the two digits based on their places, we know which two places in answer to update. 
Note that the answer array will be reversed just like before. So when we multiply a digit in the ith place of the first number by a digit in the jth place of the second number, then the ones place of the result will add to the (i+j)th place in the final answer and the tens place of the result (carry) will be added to the (i+j+1)th place in the final answer.

"""

class Solution:
	# Time: O(m*n), Space: O(m+n)
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        first = num1[::-1]
        second = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(first)):
            for j in range(len(second)):
                carry = res[i+j]
                prod = int(first[i]) * int(second[j]) + carry # 0-8
                # print("prod->", prod)
                # print("res->", res)
                carry, out = divmod(prod, 10)
                res[i+j] = out
                res[i+j+1] += carry
                # print("res->", res)
        
        if res[-1] == 0:
            res.pop()
        return "".join(str(digit) for digit in reversed(res))
                    
if __name__ == '__main__':
    s = Solution()
    print(s.multiply('2', '3'))
    print(s.multiply('123', '456'))
    print(s.multiply('408', '5'))


