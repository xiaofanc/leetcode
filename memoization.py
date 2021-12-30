# leetcode: 91.Decode Ways

def memo(f):
    m = {}
    def wrapper(*args): # new function
        if args not in m:            
            m[args] = f(*args)
            # f(self, '12') = numDecoding(self, '12')
            # m {[self, '12']: 2}
        return m[args]
    return wrapper
