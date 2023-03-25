class Solution:
    def distMoney(self, money: int, children: int) -> int:
        
        money -= children
        if money < 0:
            return -1
            
        cnt, left = money // 7, money % 7
        if cnt > children: 
            return children-1
        elif cnt == children and left > 0:
            return children-1
        else:
            if cnt == children-1 and left == 3:
                return cnt-1
            else:
                return cnt
                
            