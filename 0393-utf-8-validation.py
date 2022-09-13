class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        res = []
        for n in data:
            res.append(bin(n)[2:].zfill(8))
        # print("res->", res)
        i = 0
        while i < len(res):
            bs = 0
            for k in range(len(res[i])):
                if res[i][k] == '1':
                    bs += 1
                else:
                    break
            if bs == 0 and i == len(res)-1:
                return True
            elif bs != 0 and i == len(res)-1:
                return False
            elif bs > 4:
                return False
            # print("bs", bs)
            j = i
            while bs > 1 and j < len(res):
                j += 1
                bs -= 1
                # print("j, bs", j, bs)
                if res[j][:2] != '10':
                    return False
                if bs > 1 and j == len(res)-1:
                    return False
            i = j+1
            # print("i", i)
        return True
                
class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        # Number of bytes in the current UTF-8 character
        n_bytes = 0

        # For each integer in the data array.
        for num in data:

            # Get the binary representation. We only need the least significant 8 bits
            # for any given number.
            bin_rep = format(num, '#010b')[-8:]

            # If this is the case then we are to start processing a new UTF-8 character.
            if n_bytes == 0:

                # Get the number of 1s in the beginning of the string.
                for bit in bin_rep:
                    if bit == '0': break
                    n_bytes += 1

                # 1 byte characters
                if n_bytes == 0:
                    continue

                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                # Else, we are processing integers which represent bytes which are a part of
                # a UTF-8 character. So, they must adhere to the pattern `10xxxxxx`.
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False

            # We reduce the number of bytes to process by 1 after each integer.
            n_bytes -= 1

        # This is for the case where we might not have the complete data for
        # a particular UTF-8 character.
        return n_bytes == 0     


if __name__ == '__main__':
    s = Solution()
    print(s.validUtf8([250,145,145,145,145])) # False
    print(s.validUtf8([197,130,1])) # True



    


