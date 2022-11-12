
def convert_base(num, base):
	res = []
	while num > 0:
		res.insert(0, num % base)
		num = num // base
	return res

print(convert_base(5, 4))  # 11
print(convert_base(17, 4))  # 101
print(convert_base(21, 4))  # 111
print(convert_base(80, 4))  # 1100
