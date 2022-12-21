"""
Return an array of the k-values corresponding to a sequence of pancake flips that sort arr.

- 找到n个烧饼中最大的那个x
- 把这个最大的烧饼移到最底下
    - 翻转前x个烧饼，让x在最上面
    - 翻转前n个烧饼，让x移到最下面
"""
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        def reverse(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        def sort(cakes, n):
            # move max to the bottom
            if n == 1:
                return
            maxCake, maxCakeIdx = 0, 0
            for i in range(n):
                v = cakes[i]
                if v > maxCake:
                    maxCake = v
                    maxCakeIdx = i
            if maxCakeIdx != maxCake-1:
                # reverse until maxCake
                reverse(cakes, 0, maxCakeIdx)
                res.append(maxCakeIdx+1)
                # reverse all pancakes
                reverse(cakes, 0, n-1)
                res.append(n)
            # recursion to sort n-1
            sort(cakes, n-1)
        
        sort(arr, len(arr))
        return res
        
