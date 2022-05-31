class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # initialize all 32-bit to 0
        ans = 0
        for i in range(32):
            # ans shift to the left by 1
            ans <<= 1
            # print("res", bin(res))
            # get the current bit by logic and 1
            ans += ( n&1 )  
            # n shift to the right by 1
            n >>= 1   
        return ans

    def reverseBits(self, n: int) -> int:
        res = 0 # initialized all 32-bit by 0
        for i in range(32):
            # current bit
            bit = (n >> i) & 1
            # add to the res by or
            res = res | (bit << (31-i))
        return res
        
if __name__ == '__main__':
    s = Solution()
    rev = s.reverseBits(int('00000000000000000000000000011100', 2))
                            #111000000000000000000000000000 前面自动补0
    rev = s.reverseBits(int('00000010100101000001111010011100', 2))
    print(bin(rev)) # 00111001011110000010100101000000
    rev = s.reverseBits(int('11111111111111111111111111111101', 2))
    print(bin(rev)) # 10111111111111111111111111111111