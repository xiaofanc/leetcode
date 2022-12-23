"""
先来的那个人可以控制自己拿到所有的奇数堆或偶数堆。因为sum(奇数), sum(偶数)有大小(总数是奇数)。
所以先来的人总能赢。
"""
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True