"""
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:  # O(n)
        # remove a ')' if it is encountered when stack was already empty
        # remove a '(' if it is left on stack at end
        # use stack to store the index of brackets
        index_to_remove = set()
        stack = []
        for i in range(len(s)):
            if s[i] not in "()":
                continue
            if s[i] == '(':
                stack.append(i)
            elif stack != [] and s[i] == ')':
                stack.pop()
            else: # no matching '(' for ')'
                index_to_remove.add(i)
        # if left '(' on stack
        index_to_remove = index_to_remove.union(set(stack))
        
        string_builder = []
        for i, c in enumerate(s):
            if i not in index_to_remove:
                string_builder.append(c)
        return ''.join(string_builder)
    
    # two parse string builder
    def minRemoveToMakeValid(self, s: str) -> str: # O(n)
        # build up a string builder in the first loop that has all of the invalid ')' removed
        # for the left unmatched '(': look at the string in reverse, for each ')' there is a '(' to match with, then remove all the invalid '('
        # the last step is to reverse all characters left
        def delete_invalid_closing(string, open_symbol, close_symbol):
            string_builder = []
            balance = 0
            for c in string:
                if c == open_symbol:
                    balance += 1
                if c == close_symbol:
                    if balance == 0:
                        continue
                    else:
                        balance -= 1
                string_builder.append(c)
            return ''.join(string_builder)
        
        s = delete_invalid_closing(s, '(', ')')
        print(s)
        s = delete_invalid_closing(s[::-1], ')', '(')
        print(s)
        return s[::-1]
        

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = []

        for idx, c in enumerate(s):
            if c == "(":
                stack.append((idx, c))
            if c == ")":
                if stack:
                    stack.pop()
                else:
                    remove.append(idx)
        # print(remove, s)
        # check if "(" left in the stack
        if stack:
            for i in range(len(stack)):
                remove.append(stack[i][0] )
        
        # print(remove, s)
        return "".join(s[i] for i in range(len(s)) if i not in remove) 
                        
if __name__ == '__main__':
    s = Solution()
    print(s.minRemoveToMakeValid("lee(t(c)o)de)"))       # "lee(t(c)o)de"  
            
