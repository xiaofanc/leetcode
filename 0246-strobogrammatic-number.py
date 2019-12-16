class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        map_num = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"} 
        l, r = 0, len(num)-1
        while l <= r:
            if num[l] not in map_num:
                return False
            elif map_num[num[l]] != num[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
            
if __name__ == '__main__':
    s = Solution()
    print(s.isStrobogrammatic("69"))