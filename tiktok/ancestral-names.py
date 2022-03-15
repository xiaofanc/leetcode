"""
In some cultures, children are named after ancestors and there is a number following which represents how many ancestors have shared that name. They are often shown as Roman Numerals.
In Roman numerals, a value is not repeated more than three times. At that point, a smaller value precedes a larger value to indicate subtraction. For example, the letter I represents the number 1, and V represents 5. Reason through
the formation of 1 to 70 below, and see how it is applied in the following lines.
I, II, III. IV. V. VI. VII. VIII, IX and X represent 1 through 10.

XX XXX XL and L are 20. 30, 40. and 50.

Given a list of strings comprised of a name and a Roman numeral, sort the list first by name, then by decimal value of the Roman numeral.
For example, If you are given the names (Steven XL Steven XVI, David IX, Mary XV. Mary XIII, Mary XX the result of the sort is David IX, Mary XIII, Mary XV, Mary XX, Steven XVI, Steven XL. The result with Roman numerals is the expected
return value. Written with the numbers in decimal, they are David 9, Mary 13, Mary 15, Mary 20, Steven 16, Steven 40.

"""

def sortRoman(names):
	# Time O(NlogN), space O(N)
	# sort the list first by name, then by decimal value of the Roman numeral
	names = [name.split(" ") for name in names]
	for name in names: # [['mary', 'XX'], ['try', 'XII']]
		name.append(romanToInt(name[1]))
		name.append(" ".join(name[:2]))
	names.sort(key = lambda x: (x[0], x[2]))
	print("name sorted->", names)
	return [name[-1] for name in names]

	# arr = []
	# for name in names:
	# 	given, roman = name.split(" ")
	# 	sort_key = (given, romanToInt(roman))
	# 	arr.append((sort_key, name))
	# arr.sort()
	# return [name[-1] for name in arr]

def romanToInt(roman):
	romanmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	num = 0
	for i, v in enumerate(roman):
		if i+1 < len(roman) and romanmap.get(v) < romanmap.get(roman[i+1]):
			num -= romanmap.get(v)
		else:
			num += romanmap.get(v)
	return num

print(sortRoman(["Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XIII", "Mary XX"])) 
# ['David IX', 'Mary XIII', 'Mary XV', 'Mary XX', 'Steven XVI', 'Steven XL']





