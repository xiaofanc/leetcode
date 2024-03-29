"""
You are given a 0-indexed 2D integer array brackets where brackets[i] = [upperi, percenti] means that the ith tax bracket has an upper bound of upperi and is taxed at a rate of percenti. The brackets are sorted by upper bound (i.e. upperi-1 < upperi for 0 < i < brackets.length).

Tax is calculated as follows:

The first upper0 dollars earned are taxed at a rate of percent0.
The next upper1 - upper0 dollars earned are taxed at a rate of percent1.
The next upper2 - upper1 dollars earned are taxed at a rate of percent2.
And so on.

You are given an integer income representing the amount of money you earned. Return the amount of money that you have to pay in taxes.

Input: brackets = [[3,50],[7,10],[12,25]], income = 10
Output: 2.65000
Explanation:
The first 3 dollars you earn are taxed at 50%. You have to pay $3 * 50% = $1.50 dollars in taxes.
The next 7 - 3 = 4 dollars you earn are taxed at 10%. You have to pay $4 * 10% = $0.40 dollars in taxes.
The final 10 - 7 = 3 dollars you earn are taxed at 25%. You have to pay $3 * 25% = $0.75 dollars in taxes.
You have to pay a total of $1.50 + $0.40 + $0.75 = $2.65 dollars in taxes.

Input: brackets = [[1,0],[4,25],[5,50]], income = 2
Output: 0.25000
Explanation:
The first dollar you earn is taxed at 0%. You have to pay $1 * 0% = $0 dollars in taxes.
The second dollar you earn is taxed at 25%. You have to pay $1 * 25% = $0.25 dollars in taxes.
You have to pay a total of $0 + $0.25 = $0.25 dollars in taxes.

Input: brackets = [[2,50]], income = 0
Output: 0.00000
Explanation:
You have no income to tax, so you have to pay a total of $0 dollars in taxes.

"""
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        for i in range(len(brackets)):
            if brackets[i][0] < income:
                if i == 0:
                    tax += brackets[i][0] * brackets[i][1]
                else:
                    tax += (brackets[i][0]-brackets[i-1][0]) * brackets[i][1]
            else:
                if i == 0:
                    tax += income * brackets[i][1]
                else:
                    tax += (income - brackets[i-1][0]) * brackets[i][1]
                break
        return tax * 0.01

if __name__ == '__main__':
	s = Solution()
	print(s.calculateTax([[2,50]], 0)) # 0 


	
                