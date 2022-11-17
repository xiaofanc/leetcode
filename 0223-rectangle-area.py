class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        total = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)

        if ax2 <= bx1 or bx2 <= ax1:
            return total
        elif ay2 <= by1 or by2 <= ay1:
            return total
        else:
            left = max(ax1, bx1)
            right = min(ax2, bx2)
            bottom = max(ay1, by1)
            up = min(ay2, by2)
            return total - (right-left)*(up-bottom)

if __name__ == '__main__':
    s = Solution()
    print(s.computeArea(-3,0,3,4,0,-1,9,2)) # 45