"""
You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:

All money must be distributed.
Everyone must receive at least 1 dollar.
Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.

"""
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        res = 0
        for i in range(children):
            money -= 7
            # if not enough money to give to the next child or
            # money = 3 and only one child left, give more money to the current child
            if money < 0 or (money == 3 and i == children-2):
                return res
            else:
                res += 1    
        # if more money is left, give all to the last child
        if money > 0:
            return res-1
        return res
