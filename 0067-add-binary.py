class Solution:
    def addBinary(self, a, b):
        result, carry = '', 0
        i, j = len(a)-1, len(b)-1
        print(result, carry, i, j)
        while i >= 0 or j >= 0 or carry:
            curval = (i >= 0 and a[i] == '1') + (j >= 0 and b[j] == '1')
            carry, res = divmod(curval+carry, 2)
            result = str(res) + result
            print(i, j, curval, carry, res, result)
            i -= 1
            j -= 1
        return result
        
        
s=Solution()
print(s.addBinary("1010","1011"))