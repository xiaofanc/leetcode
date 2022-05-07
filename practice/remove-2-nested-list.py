nested_list = [[1,2,3], [2,3, [2,4, [2]]]]

def remove2(nested):
    res = []
    for i in nested:
        if isinstance(i, int) and i != 2:
            res.append(i)
        elif isinstance(i, list):
            res.append(remove2(i))
    return res

def add3(nested):
    res = []
    for i in nested:
        if isinstance(i, int):
            if i != 2:
                res.append(i)
            else:
                res.append(i)
                res.append(3) 
        elif isinstance(i, list):
            res.append(add3(i))
    return res

# nest 1 or 4
def nest1or4(nested):
    res = []
    for i in nested:
        if isinstance(i, int):
            if i == 1 or i == 4:
                res.append([i])
            else:
                res.append(i)
        elif isinstance(i, list):
            res.append(nest1or4(i))
    return res

# flatten list
def flatten(nested):
    res = []
    for i in nested:
        if isinstance(i, int):
            res.append(i)
        elif isinstance(i, list):
            res.extend(flatten(i))
    return res

print(remove2(nested_list)) # [[1,3], [3, [4, []]]]
print(add3(nested_list)) # [[1,2,3,3], [2,3,3, [2,3,4, [2,3]]]]
print(nest1or4(nested_list)) # [[[1], 2, 3], [2, 3, [2, [4], [2]]]]
print(flatten(nested_list)) # [1, 2, 3, 2, 3, 2, 4, 2]



