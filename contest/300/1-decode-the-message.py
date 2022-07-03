"""
Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".
"""

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keyMap = {}
        idx = 97
        for char in key:
            if char == " ":
                continue
            if char not in keyMap:
                keyMap[char] = chr(idx)
                idx += 1
        encode = ""
        for char in message:
            if char == " ":
                encode += " "
            else:
                encode += keyMap[char]
        return encode
