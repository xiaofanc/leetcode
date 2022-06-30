d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)

print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)

print(d)

import collections

test = {'one':1, 'two':1}
test1 = {'two':2}

for k, v in test1.items():
	test.update(collections.Counter(k))

print(test)


