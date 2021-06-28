class Solution:

    # time: O(n), space: O(n)
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxc = max(candies)
        output = []
        for candy in candies:
            if candy + extraCandies >= maxc:
                output.append(True)
            else:
                output.append(False)
        return output

    # time: O(n), space: O(1)
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        for i in range(len(candies)):
            
            if candies[i]+extraCandies>=m:
                candies[i]=True
            else:
                candies[i]=False
        return candies

    # time: O(n), space: O(1)
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        return [True if candy + extraCandies >= m else False for candy in candies]

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return list(map(lambda x: x + extraCandies >= max(candies), candies))

if __name__ == '__main__':
    s = Solution()
    print(s.kidsWithCandies([2,3,5,1,3], 3))
    print(s.kidsWithCandies([4,2,1,1,2], 1))






    