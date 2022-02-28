"""
keep the space before //:
"  // variable declaration "

combine the string:
["a/*comment", "line", "more_comment*/b"] -> ["ab"]

buffer was added only when */ appears !!

"""


class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res, buffer, block_comment_open = [], '', False
        for line in source:
            i = 0
            while i < len(line):
                char = line[i]
                # "//" -> Line comment.
                if char == '/' and (i + 1) < len(line) and line[i + 1] == '/' and not block_comment_open:
                    i = len(line) # Advance pointer to end of current line.
                # "/*" -> Start of block comment.
                elif char == '/' and (i + 1) < len(line) and line[i + 1] == '*' and not block_comment_open:
                    block_comment_open = True
                    i += 1
                # "*/" -> End of block comment.
                elif char == '*' and (i + 1) < len(line) and line[i + 1] == '/' and block_comment_open:
                    block_comment_open = False
                    i += 1
                # Normal character. Append to buffer if not in block comment.
                elif not block_comment_open:
                    buffer += char
                    # print('buffer:', buffer, len(buffer))
                i += 1
            # print("block_comment_open->", block_comment_open)
            # clean buffer only after cleaning the comments
            if buffer and not block_comment_open:
                res.append(buffer)
                buffer = ''
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.removeComments(["a/*comment", "line", "more_comment*/b"])) # "ab"
	print(s.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])) # ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]


