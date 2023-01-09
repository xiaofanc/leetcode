class Solution:
    # Backtracking
    # Time: O(lgn^lgn), Each of the nodes will explore lgn factors. The depth of the tree will also be lgn.
    # O(lgn) = O(sqrt(n))
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        if n == 1:
            return []
        target = n
        def backtrack(start, n, comb):
            # use start to exclude duplicates like [3,2,2]
            # exclude [12]
            if len(comb) > 0:
                res.append(comb + [n])

            # [2,6], [2,2,3], [3,4]
            for i in range(start, int(math.sqrt(n))+1):
                if n % i == 0:
                    comb.append(i)
                    backtrack(i, n//i, comb)
                    comb.pop()
        backtrack(2, n, [])
        return res

    # DFS
    def getFactors(self, n: int) -> List[List[int]]:
        def factors(n, i):
            result = []
            while i * i <= n:
                if n % i == 0:
                    # [2,6] + [2,2,3] + [3,4]
                    result += [[i, n // i]] + [[i] + s for s in factors(n // i, i)]
                    # print("result, ", result)
                i += 1
            return result
        return factors(n, 2)

    # DFS
    def getFactors(self, n: int) -> List[List[int]]:
        def helper(start, n):
            res = []
            if n == 1:
                return []
            for i in range(start, int(math.sqrt(n))+1):
                if n % i == 0:
                    res += [[i, n // i]] + [[i] + s for s in helper(i, n//i)]
            return res
        return helper(2, n)

    # the idea is to iteratively divide the last number in the factor combo into smaller numbers
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        def helper(cur, i):
            num = cur.pop()
            while i*i <= num:
                if num % i == 0:
                    res.append(cur + [i, num//i])
                    # start from i to avoid duplication
                    helper(cur + [i, num//i], i)
                i += 1
        helper([n], 2)
        return res



        