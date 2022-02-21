class Solution:
    # Time complexity : as discussed above, there is not more than 27 combinations to check.
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
                        
if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("25525511135")) # ["255.255.11.135","255.255.111.35"]

