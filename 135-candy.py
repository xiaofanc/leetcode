class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) < 2:
            return len(ratings)
            
        res = [1]*len(ratings)
        for i in range(1, len(ratings)):
            # look left
            # if res[i] already > res[i-1], not need to add 1
            # res[i] must have more candies than res[i-1] if ratings[i] > ratings[i-1]
            if ratings[i] > ratings[i-1] and res[i] <= res[i-1]:
                res[i] = res[i-1] + 1
        for j in range(len(ratings)-1, 0, -1):
            # look right
            if ratings[j-1] > ratings[j] and res[j-1] <= res[j]:
                res[j-1] = res[j] + 1
        return sum(res)

if __name__ == '__main__':
    s = Solution()
    print(s.candy([1,2,87,87,87,2,1])) # 13
    print(s.candy([1,0,2])) # 5