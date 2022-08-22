"""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

There are 3 available spots to place the first dot
           25525511135
first dot:    2           55         255
second dot: 5 55 552   5 52 525    2 25 255
....
There are 4 dots at most. We will return if there are more than 4 integers

Time: 3^4
Space: constant

"""


class Solution:
    # Time complexity : as discussed above, there is not more than 3x3x3 = 27 combinations to check.
    # Space complexity : constant space to keep the solutions, not more than 19 valid IP addresses.
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(segment):
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1
        
        def update_output(curr_pos):
            segment = s[curr_pos+1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()
                
        def backtrack(prev_pos = -1, dots = 3):
            for cur_pos in range(prev_pos + 1, min(n-1, prev_pos + 4)):
                segment = s[prev_pos+1:cur_pos+1]
                if valid(segment):
                    segments.append(segment)
                    if dots - 1 == 0:
                        update_output(cur_pos)
                    else:
                        backtrack(cur_pos, dots-1)
                    segments.pop()
        n = len(s)
        segments, output = [], []
        backtrack()
        return output

    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        # length of s cannot be > 12
        if len(s) > 12:
            return res
        
        def backtrack(i, dots, curIP):
            # i is the start position of substring
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            if dots > 4:
                return
            # j is the end position of the substring - dot position
            # iterate over three available slots to place a dot if len(s[i:j+1]) > 3 then it will be larger than 255
            for j in range(i, min(i+3, len(s))):
                # start position can be 0 only if the segment is "0"
                if int(s[i:j+1]) < 256 and (s[i] != "0" or i == j):
                    backtrack(j+1, dots+1, curIP + s[i:j+1] + ".")
        backtrack(0, 0, "")
        return res                        

    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def backtrack(i, comb):
            # i is the start position of substring
            if i == len(s) and len(comb) == 4:
                res.append(".".join(comb[:]))
                return
            if len(comb) > 4:
                return
            # j is the end position of the substring - dot position
            for j in range(i, min(i+3,len(s))):
                substring = s[i:j+1]                
                if substring == '0' or (0 < int(substring) <= 255 and substring[0] != '0'):
                    comb.append(substring)
                    backtrack(j+1, comb)
                    comb.pop()
        backtrack(0, [])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("25525511135")) # ["255.255.11.135","255.255.111.35"]
    print(s.restoreIpAddresses("0000")) # ["0.0.0.0"]
    print(s.restoreIpAddresses("101023")) # ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

