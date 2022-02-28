"""
Think of it as a tree and now create a dictionary of ppid. Key is ppid and values are the list of its immediate children.
Now search through the dictionary in BFS fashion to get all the processes that will be killed.
"""

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        child = collections.defaultdict(list)
        for c, p in zip(pid, ppid):
            child[p].append(c)
            
        queue = [kill]
        ans = []
        while queue:
            p = queue.pop()
            ans.append(p)
            if p in child:
                queue.extend(child[p])
        return ans

if __name__ == '__main__':
	s = Solution()
	print(s.killProcess([1,3,10,5], [3,0,5,3], 5)) # [5,10]