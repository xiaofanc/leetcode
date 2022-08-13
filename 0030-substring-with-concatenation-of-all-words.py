"""
solution 1: check window when char is a possible start
solution 2: fixed sliding window = L
"""

class Solution:
	# when char is the start then check the window
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        starts = set(word[0] for word in words)
        l = len(words[0])
        L = len(words) * l
        target = collections.Counter(words)
        res = []
        for i in range(len(s)-L+1):  # remove TLE
            if s[i] in starts:   # repeat work
                start = i
                window = {}
                j = i+l
                # print("i->", i)
                while j < min(i+L+1, len(s)+1):
                    # print("j->", j, s[start:j])
                    if s[start:j] not in target:
                        break
                    else:
                        window[s[start:j]] = window.get(s[start:j], 0) + 1
                        if window[s[start:j]] > target[s[start:j]]:
                            break
                        if window == target:
                            res.append(i)
                            break
                        start = j
                        # print("window->", window)
                    j += l
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])) # 8

	

                
                        
                        
                        
                
                
                

                
                        
                        
                        
                
                
                
