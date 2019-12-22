class Solution:
    def repeatedStringMatch0(self, A: str, B: str) -> int:
        q = (len(B) - 1) // len(A) + 1 # the least number for len(B) <= len(A*q)
        for i in range(2):
            if B in A*(q+i): return q+i
        return -1

    def repeatedStringMatch1(self, A: str, B: str) -> int:
        times = -(-len(B) // len(A)) # Equal to ceil(len(b) / len(a)); -7 // 4 = -2
        return times * (B in A*times) or (times+1) * (B in A*(times+1)) or -1

    def repeatedStringMatch2(self, A: str, B: str) -> int:
        temp = ""
        count = 0
        while len(temp) < len(B):
            temp += A
            count += 1
            if B in temp:
                return count
        temp += A
        if B in temp:
            return count+1
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.repeatedStringMatch0("abcd", "cdabcdab") == 3)
    #print(s.repeatedStringMatch1("abcd", "cdabcdab") == 3)
    #print(s.repeatedStringMatch2("abcd", "cdabcdab") == 3)