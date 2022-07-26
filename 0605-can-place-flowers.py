class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while n > 0 and i < len(flowerbed):
            # when can plant the flower
            if flowerbed[i] == 0 and (i-1 < 0 or flowerbed[i-1] == 0) and (i+1 == len(flowerbed) or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            i += 1
        return n == 0

    # optimize
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while n > 0 and i < len(flowerbed):
            if flowerbed[i] == 0 and (i-1 < 0 or flowerbed[i-1] == 0) and (i+1 == len(flowerbed) or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0: # early stop
                    return True
                i += 1     # next place cannot place flowers
            i += 1         # move to the next place
        return n == 0

if __name__ == '__main__':
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1], 1)) # True
    print(s.canPlaceFlowers([0], 1)) # True
    print(s.canPlaceFlowers([1], 1)) # False