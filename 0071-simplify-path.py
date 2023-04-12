"""
"/a/./b/../../c/" -> "/c"
"/home/" -> "/home"
"/../" -> "/"
"/home//foo/" -> "/home/foo"
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        res = "/"
        directory = []
        parts = path.split("/")  # ['', 'home', '', 'foo', '']
        for i, part in enumerate(parts):
            if part == ".":
                continue
            elif part == "..":
                if directory:
                    directory.pop()
            elif part != "":
                directory.append(part)
        return res + "/".join(directory)


