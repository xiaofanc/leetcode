"""
"/leetcode", parent ""
"/x/d", parent "/x"
"/x/d/t", parent "/x/d"

"""

class FileSystem:

    def __init__(self):
        self.path = {}

    def createPath(self, path: str, value: int) -> bool:
        # step 1: basic path validation
        if path == "" or path == "/" or path in self.path:
            return False
        # step 2: check if parent doesn't exist. Note that "/leet" does not have parent, but it is valid path
        parent = path[:path.rfind("/")]
        # print("parent->", parent)
        if len(parent) > 1 and parent not in self.path:
            return False
        # step 3: add path to dictionary and return True
        self.path[path] = value
        return True

    def get(self, path: str) -> int:
        return self.path.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)