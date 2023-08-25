class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        c = 0
        s = 0
        prev = 1
        exclude = set()
        while c < n:
            if k < prev:
                s += prev
                c += 1
            else:
                if prev not in exclude:
                    s += prev
                    c += 1
                    exclude.add(k-prev)
            prev += 1
        return s
            
