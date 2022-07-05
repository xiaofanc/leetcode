class TreeNode:
    def __init__(self):
        self.child = defaultdict(TreeNode)
        self.content = ""
        self.isFile = False
    
    def __str__(self):
        return 'N(%s, %s)' % (self.child.keys(), self.files.keys())
        
class FileSystem:

    def __init__(self):
        self.fileSystem = TreeNode()
        
    def ls(self, path: str) -> List[str]:
        node = self.fileSystem
        path = path.split("/")
        for p in path:
            if not p:
                continue
            node = node.child.get(p)
        if node.isFile:
            return [path[-1]]
        ans = [i for i in node.child.keys()]
        if not ans:
            return ans
        ans.sort()
        return ans

    def mkdir(self, path: str) -> None:
        node = self.fileSystem
        path = path.split("/")
        for d in path:
            if not d:
                continue
            node = node.child[d]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.fileSystem
        path = filePath.split("/")
        for d in path:
            if not d:
                continue
            node = node.child[d]
        node.content += content
        node.isFile = True

    def readContentFromFile(self, filePath: str) -> str:
        node = self.fileSystem
        path = filePath.split("/")
        for d in path:
            if not d:
                continue
            node = node.child[d]
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)



