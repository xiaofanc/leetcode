class Solution:
	def isIsomorphic1(self, s, t):
	    d1, d2 = {}, {}
	    for i, val in enumerate(s):
	        d1[val] = d1.get(val, []) + [i]
	    for i, val in enumerate(t):
	        d2[val] = d2.get(val, []) + [i]
	    print(d1,d2)
	    return sorted(d1.values()) == sorted(d2.values())
	        
	def isIsomorphic2(self, s, t):
	    d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
	    for i, val in enumerate(s):
	        d1[ord(val)].append(i)
	    for i, val in enumerate(t):
	        d2[ord(val)].append(i)
	    print(d1)
	    print(d2)
	    return sorted(d1) == sorted(d2)
	    
	def isIsomorphic3(self, s, t):
	    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
	    
	def isIsomorphic4(self, s, t): 
	    return [s.find(i) for i in s] == [t.find(j) for j in t]
	    
	def isIsomorphic5(self, s, t):
	    return list(map(s.find, s)) == list(map(t.find, t))
	
	def isIsomorphic6(self, s, t):
	    d1, d2 = [0 for _ in range(256)], [0 for _ in range(256)]
	    for i in range(len(s)):
	        if d1[ord(s[i])] != d2[ord(t[i])]:
	            return False
	        d1[ord(s[i])] = i+1
	        d2[ord(t[i])] = i+1
	    print(d1)
	    print(d2)
	    return True

if __name__ == '__main__':
	s = Solution()
	print(s.isIsomorphic1("egg","add"))
	print(s.isIsomorphic2("egg","add"))
	print(s.isIsomorphic3("egg","add"))
	print(s.isIsomorphic4("egg","add"))
	print(s.isIsomorphic5("egg","add"))
	print(s.isIsomorphic6("egg","add"))
