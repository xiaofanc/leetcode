class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compress(string):
            stack = []
            for c in string:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)
        return compress(s) == compress(t)

    # Space: O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        def F(S):
            skip = 0 # remember to skip how many chars
            for x in reversed(S):
                if x == "#":
                    skip += 1
                elif skip: # skip char
                    skip -= 1
                else:
                    yield x
        # print(list(itertools.zip_longest(F(s), F(t))))  # [('d', 'b'), ('c', None)]
        return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))

if __name__ == '__main__':
    s = Solution()
    print(s.backspaceCompare("y#fo##f", "y#f#o##f")) # True
    print(s.backspaceCompare("a#cd", "b")) # False
