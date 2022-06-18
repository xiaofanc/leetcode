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

if __name__ == '__main__':
	s = Codec()
	enc = s.encode(["He7#llo","World"])
	print(enc)  # 7#He7#llo5#World
	dec = s.decode(enc)
	print(dec)  # ['He7#llo', 'World']


