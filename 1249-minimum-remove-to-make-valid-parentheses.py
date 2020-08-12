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
    

        
        
                
                
            
