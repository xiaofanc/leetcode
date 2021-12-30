
class Solution:
    # Time: O(k*(n!/(n-k)!k!))
    # Space: O(n!/(n-k)!k!)
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
        
        output = []
        backtrack()
        return output

if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]