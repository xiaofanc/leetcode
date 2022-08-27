class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        Let's work through an example like N = 128.
        In the last line, 'for cand in itertools.permutations(str(N))' will
        iterate through the six possibilities cand = ('1', '2', '8'),
        cand = ('1', '8', '2'), cand = ('2', '1', '8'), and so on.

        The check cand[0] != '0' is a check that the candidate permutation
        does not have a leading zero.

        The check bin(int("".join(cand))).count('1') == 1 is a check that cand
        represents a power of 2: namely, that the number of ones in its binary
        representation is 1.

        Time Complexity: O((logN)!xlogN). Note that logN is the number of digits in the binary representation of N. For each of (logN)! permutations of the digits of N, we need to check that it is a power of 2 in O(logN) time.

        Space Complexity: O(logN), the space used by A (or cand in Python).
        """
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(N)))