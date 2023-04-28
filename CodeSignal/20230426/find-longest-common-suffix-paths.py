"""
find the longest common suffix for paths

paths = ["/Redfin/d/../a.txt","/Redfin/a.txt","/Redfin/t/../a.txt"]
paths = ["/users/a.txt","/admin/a.txt","/Redfin/a.txt"]
paths = ["/temp.txt"]
"""

def longest_common_suffix(paths):
	clean = []
	for path in paths:
		parts = path.split("/")
		stack = []
		for p in parts:
			if p == "..":
				if stack:
					stack.pop()
			else:
				stack.append(p) # "" also appended
		clean.append("/".join(stack))
	# print("clean ", clean)
	# find the LCS
	LCS = clean[0].split("/")
	for i in range(1, len(clean)):
		path = clean[i].split("/")
		a, b = len(LCS)-1, len(path)-1
		while a >= 0 and b >= 0 and LCS[a] == path[b]:
			a -= 1
			b -= 1
		LCS = LCS[a+1:]       # common suffix with path
	# print("LCS ", LCS)
	if len(LCS) == 0:
		return ""             # no common suffix
	elif LCS[0] == "":
		return "/".join(LCS)  # common suffix starts from the root
	else: 
		return "/" + "/".join(LCS) # common suffix in the middle


paths = ["/Redfin/d/../a.txt","/Redfin/a.txt","/Redfin/t/../a.txt"]
print(longest_common_suffix(paths))
paths = ["/users/a.txt","/admin/a.txt","/Redfin/a.txt"]
print(longest_common_suffix(paths))
paths = ["/temp.txt"]
print(longest_common_suffix(paths))


