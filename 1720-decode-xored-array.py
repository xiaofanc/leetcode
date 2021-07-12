"""
a = b XOR c then b = a XOR c, c = a XOR b
b = b XOR c XOR c
  = b XOR (c XOR c)
  = b XOR 0
  = b

1 XOR 0 = 1
0 XOR 1 = 1
1 XOR 1 = 0
0 XOR 0 = 0

2 XOR 3 = 10 XOR 11 = 1
"""
class Solution:

    # time: O(n), space: O(n)
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # encoded[i] = arr[i] XOR arr[i+1]
        # arr[i] = encoded[i-1] XOR arr[i-1]
        res = [first]
        for i in range(1, len(encoded)+1):
            res.append(encoded[i-1] ^ res[i-1])
        return res

    # time: O(n), space: O(1)
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # encoded[i] = arr[i] XOR arr[i+1]
        # arr[i] = encoded[i-1] XOR arr[i-1]
        encoded.insert(0, first)
        for i in range(1, len(encoded)):
            encoded[i] = encoded[i-1] ^ encoded[i]
        return encoded

    def decode(self, encoded: List[int], first: int) -> List[int]:
        return itertools.accumulate(encoded, operator.xor, initial=first)
        
if __name__ == '__main__':
    s = Solution()
    print(s.decode([1,2,3], 1))