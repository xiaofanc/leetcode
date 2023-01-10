"""
1. a decimal or an integer must have at least one digit
- Let's use a variable seenDigit to indicate whether we have seen a digit yet.

2. if sign exists in the s, it must be in the beginning or right after e
- Therefore, if we see a sign, and it is not the first character of the input, and does not come immediately after an exponent ("e" or "E"), then we know the number is not valid.

3. if e exists in the s, it must follow a decimal or an int, and must be followed by an int
- There cannot be more than one exponent in a valid number, so we will use a variable seenExponent to indicate whether we have already seen an exponent.
- An exponent must appear after a decimal number or an integer. This means if we see an exponent, we must have already seen a digit.

4. if dot exists in the s, A decimal number should only contain one dot. Integers cannot contain dots.
- There cannot be more than one dot in a valid number, since only integers are allowed after an exponent, so there cannot be more than one decimal number. We will use a variable seenDot to indicate whether we have seen a dot.
- If we see a dot appear after an exponent, the number is not valid, because integers cannot have dots.
"""

    def isNumber(self, s: str) -> bool:
        seenDigit, seenExponent, seenDot = False, False, False
        for i, ch in enumerate(s):
            if ch.isnumeric():
                seenDigit = True
            elif ch in "+-":
                # in the beginning or after e
                if i > 0 and s[i-1].lower() != "e":
                    return False
            elif ch in "Ee":
                # e9 returns False, 1e9 returns True
                if seenExponent or not seenDigit:
                    return False
                seenExponent = True
                # reset since after e, we must have an int
                seenDigit = False
            elif ch == ".":
                # e2.5 returns False
                if seenExponent or seenDot:
                    return False
                seenDot = True
            else:
                return False
        return seenDigit


        



