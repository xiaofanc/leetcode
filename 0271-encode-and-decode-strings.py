"""
encode and decode list of strs
"""


class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            char = s[j+1:j+l+1]
            res.append(char)
            i = j+l+1
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []
        while i < len(s):
            pos = s.index("#", 1)  # position of first #
            l = int(s[i:pos])
            res.append(s[pos+1:pos+l+1])
            s = s[pos+l+1:]
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        while s:
            l, s = s.split("#", 1)  # 5, hello5#world
            res.append(s[:int(l)])
            s = s[int(l):]
        return res
        
if __name__ == '__main__':
	s = Codec()
	enc = s.encode(["He7#llo","World"])
	print(enc)  # 7#He7#llo5#World
	dec = s.decode(enc)
	print(dec)  # ['He7#llo', 'World']


