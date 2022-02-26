class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                neighbors = [img[x][y] for x in [i-1, i, i+1] for y in [j-1, j, j+1] if 0 <= x < m and 0 <= y < n]
                ans[i][j] = sum(neighbors) // len(neighbors)
        return ans
            
if __name__ == '__main__':
    s = Solution()
    print(s.imageSmoother([[1,1,1],[1,0,1],[1,1,1]])) # [[0,0,0],[0,0,0],[0,0,0]]