"""
split arr into two groups with sum(A) > sum(B) and A has the smallest number
"""
class Solution:
    def minimalHeaviestSetA(arr):
        # Write your code here
        if not arr:
            return []
        arr.sort()
        total = sum(arr)
        A = []
        sumA = 0
        for i in range(len(arr)-1,-1,-1):
            A.append(arr[i])
            sumA += arr[i]
            if sumA > total/2:
                break
        return A[::-1]
            
if __name__ == '__main__':
    arr = [3,7,5,6,2]  
    s = Solution()
    print(s.minimalHeaviestSetA(arr)) # A = [6,7]

