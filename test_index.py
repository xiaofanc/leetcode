a = list("abcded")
a = list("abcdedeeddd")
print(a.index("a"))
print(a.index("b"))
print(a.index("c"))
print(a.index("d"))
rev = a[::-1]
print(rev.index("d"))
print(len(a)-rev.index("d")-a.index("d"))
