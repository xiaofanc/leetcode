import fileinput

args = []
for line in fileinput.input():
    args.append(line)

words = args[0].split()
alpha = int(args[1])
    
class Graph:
    def __init__(self, numVertices):
        self.adjList = [[] for i in range(numVertices)]

    def addEdge(self, startVertex, endVertex):
        self.adjList[startVertex].append(endVertex)
    
    def getNoOfVertices(self):
        return len(self.adjList)
    
    def topologicalSortUtil(self, currentVertex, visited, stack):
        visited[currentVertex] = True
        for adjVertex in self.adjList[currentVertex]:
            if not visited[adjVertex]:
                self.topologicalSortUtil(adjVertex, visited, stack)
        
        stack.append(currentVertex)
    
    def topologicalSort(self):
        stack = []
        visited = [False for i in range(self.getNoOfVertices())]
        for i in range(self.getNoOfVertices()):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        
        letters = []
        
        while (len(stack) > 0):
            letters.append(chr(ord('a') + stack.pop()))
        
        return letters

"""
This function finds and returns the order
of characers from a sorted array of words.
alpha is number of possible alphabets 
starting from 'a'. For simplicity, this
function is written in a way that only
first 'alpha' characters can be  
in words array. For example if alpha
is 7, then words[] should contain words
having only 'a', 'b','c' 'd', 'e', 'f', 'g' 

Graph class
 Graph(numVertices)
 addEdge(startVertex, endVertex)
 topologicalSort() 
    rtype: List[char] 
"""
from collections import defaultdict, deque
def printOrder(words, alpha):
    adjList = defaultdict(set)
    inDegree = {}
    for i in range(len(words)-1):
        w1 = words[i]    
        w2 = words[i+1]
        minlen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
            return ''
        for a, b in zip(w1, w2):
            if a != b:
                adjList[a].add(b)
                inDegree[b] = inDegree.get(b, 0) + 1
                break
    res = []
    queue = deque()
    for i in range(alpha):
        char = chr(ord('a') + i)
        if char not in inDegree:
            queue.append(char)
    while queue:
        char = queue.popleft()
        res.append(char)
        for nei in adjList[char]:
            inDegree[nei] -= 1
            if inDegree[nei] == 0:
                queue.append(nei)
                del inDegree[nei]
    if len(res) < len(inDegree):
        return ''
    return res
                
    

order = printOrder(words, alpha)

for letter in order:
    print(letter, end=' ')