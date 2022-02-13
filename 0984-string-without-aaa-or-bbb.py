"""
Given two integers a and b, return any string s such that:

s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.

(4,4) -> "bbabbaaa" does not work, "abababab"

"""

class Solution:
	# Time Complexity: O(a+b)
	# This method does not consider that a and b will generate invalid string
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        
        # when to write A:
        # case 1: "xxxxxbb", case 2: "xxxxab/ba", a >= b
        while (a > 0 or b > 0):
            writeA = False
            if len(res) >=2 and (res[-1] == res[-2]):
                if res[-1] == "b":
                    writeA = True
            else:
                if a >= b:
                    writeA = True
            
            if writeA:
                res.append("a")
                a -= 1
            else:
                res.append("b")
                b -= 1
                
        return "".join(res)


    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ""
        
        while a or b:
            if res[-2:] == "aa":
                res += "b"
                b -= 1
            elif res[-2:] == "bb":
                res += "a"
                a -= 1
            elif a > b:
                res += "a"
                a -= 1
            else:
                res += "b"
                b -= 1
        
        return res

    def strWithout3a3b(self, a: int, b: int) -> str:
        if a * b == 0:
            return a * "a" + b * "b"
        if a == b:
            return "ab" * a
        if a > b:
            return "aab" + self.strWithout3a3b(a-2, b-1)
        return self.strWithout3a3b(a-1, b-2) + "abb"
        
if __name__ == '__main__':
	s = Solution()
	print(s.strWithout3a3b(4, 4))  # "abababab"



