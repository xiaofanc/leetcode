class Solution:
    def countDigits(self, num: int) -> int:
        cnt = 0
        for d in str(num):
            if num % int(d) == 0:
                cnt += 1
        return cnt