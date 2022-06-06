

from collections import deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        less = []
        for pair in zip(words, words[1:]):
            #print(*pair)
            for a, b in zip(*pair):
                # compare the first different str
                if a != b:
                    less.append(a+b)
                    #print(less)
                    break
        chars = set("".join(words))
        print('less', less, 'chars', chars)
        order = []
        while less:
            print('chars',chars, list(zip(*less))[1])
            #free is the char that does not have pointer
            free = chars - set(list(zip(*less))[1])
            print("free", free)
            if not free:
                return ""
            order += free
            #delete char with free as the first char from less
            less = list(filter(free.isdisjoint, less))
            print('less', less, 'order', order)
            chars -= free
        return "".join(order + list(chars))

    # BFS + topological sort
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = {c:0 for word in words for c in word}
        # convert the relationship to adj list, Time: O(C)
        for w1, w2 in zip(words, words[1:]):
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for c, d in zip(w1, w2): # keep the min len
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
        # repeatly pick off nodes with indegree = 0, Time: O(V+E)
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)
        # if not all chars in the queue, then there is a cycle
        if len(res) < len(in_degree):
            return ""
        return "".join(res)

    # DFS
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {} # True: current path, False: visited
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for d in adj[c]:
                if dfs(d):
                    return True # loop
            visit[c] = False
            # post order DFS
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        res = res[::-1]
        return "".join(res)

if __name__ == '__main__':
    s = Solution()
    print(s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
    print(s.alienOrder(["z","z"]))      # "z"
    print(s.alienOrder(["zy","zx"]))    # "zyx", "yxz", "yzx"
    print(s.alienOrder(["ac","ab","b"]))    # "zyx", "yxz", "yzx"



