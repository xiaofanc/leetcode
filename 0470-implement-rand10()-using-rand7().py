"""
Generate a from 1 to 7 and b from 1 to 7, then we have 7x7 = 49 options. Let us create number c = (a-1)*7 + b, then we can show that c is number between 1 and 49: substitute all possible values for a and b and you will see.
Now, let us divide these number into groups: [1,10]; [11;20]; [21;30]; [31;40]; [41;49]. If we get into one of the first four group we are happy: there is ten number in each group, so we just return (c-1)%10 + 1.
If we are in the fifth group, we are not happy, there are only 9 numbers in this group and we need 10, use 9 is not fair. So in these case, we say, that our experiment was not working, and we just start it all over again! That is all.
"""

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        idx = 41
        while idx > 40:
            a, b = rand7(), rand7()
            idx = (a-1) * 7 + b
        return (idx-1) % 10 + 1
            
    def rand10(self):
        """
        :rtype: int
        """
        c = (rand7()-1) * 7 + rand7()
        return (c-1) % 10 + 1 if c <= 40 else self.rand10()   




             