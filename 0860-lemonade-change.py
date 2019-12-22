from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5, count_10 = 0, 0
        for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10:
                if count_5 < 1:
                    return False
                count_10 += 1
                count_5  -= 1
            else: # bill == 20
                if count_10 >= 1 and count_5 >= 1:
                    count_10 -= 1
                    count_5  -= 1
                elif count_5 >= 3:
                    count_5  -= 3
                else:
                    return False
        return True
            
if __name__ == '__main__':
    s = Solution()
    print(s.lemonadeChange([5,5,5,10,20]))