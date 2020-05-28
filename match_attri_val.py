attributes  =   ['name',    'dob',  'gender']
values  =  \
[['jason',  '2000-01-01',   'male'], 
['mike',    '1999-01-01',   'male'],
['nancy',   '2001-02-01',   'female']]

# expected    outout:
#[{'name':'jason',  'dob':'2000-01-01', 'gender':'male'},    
# {'name':'mike',   'dob':'1999-01-01', 'gender':'male'},    
# {'name':'nancy',  'dob':'2001-02-01', 'gender':'female'}]
out = [dict(zip(attributes, v)) for v in values]
print(out)

def match(attributes, values):
    matches = []
    n = len(attributes)
    for i in range(n):
        match = {}
        for val, key in zip(values[i], attributes):
            match[key] = val
        matches.append(match)
    return matches



print(match(['name',    'dob',  'gender'], [['jason',  '2000-01-01',   'male'], ['mike',    '1999-01-01',   'male'], ['nancy',   '2001-02-01',   'female']]))
