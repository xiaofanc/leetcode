

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks:
            freq[ord(t)-ord('A')] += 1
        
        freq.sort()
        max_f = freq.pop()
        # Define the max possible idle time
        max_idle = n * (max_f-1)
        # remove idle time that can be filled
        for f in freq:
            max_idle -= min(max_f-1, f)
        max_idle = max(0, max_idle)
        return max_idle + len(tasks)

if __name__ == '__main__':
	s = Solution()
	print(s.leastInterval(["A","A","A","B","B","B"], 2))  # 8