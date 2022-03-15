"""
A company has invented a new type of printing tech:
It is a circular printer wheel with letters A to Z in sequence. It wraps so that A and Z are adjacent. The printer has a printer that is initially at 'A'. Moving from any char to any adjacent char takes 1 second. It can move in either direction. Given a string of letters, what is the minimum time needed to print the string?

For example:
s = "BZA"
Total time to print s is 1+2+1 = 4 second
"""

# Time: O(N), Space: O(1)
def getTime(s):
	time = 0
	for i in range(len(s)):
		if i == 0:
			diff = ord(s[i])-ord('A')
		else:
			diff = abs(ord(s[i])-ord(s[i-1]))
		time += min(diff, 26-diff)
	return time

print(getTime("BZA")) # 4
print(getTime("AZGB")) # 13
print(getTime("ZNMD")) # 23