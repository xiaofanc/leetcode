class Node:
    def __init__(self, key, prev = None, next = None):
        self.key = key
        self.prev = prev
        self.next = next

class BrowserHistory:
    # doubly linked list
    def __init__(self, homepage: str):
        head = Node(homepage)
        self.cur = head

    def visit(self, url: str) -> None:
        newNode = Node(url)
        # clear up forward history
        self.cur.next = newNode
        newNode.prev = self.cur
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        cur = self.cur
        while cur.prev and steps > 0:
            cur = cur.prev
            steps -= 1
        self.cur = cur
        return cur.key

    def forward(self, steps: int) -> str:
        cur = self.cur
        while cur.next and steps > 0:
            cur = cur.next
            steps -= 1
        self.cur = cur
        return cur.key

class BrowserHistory:
    # two stacks
    def __init__(self, homepage: str):
        self.current = homepage  # pointers
        self.history, self.future = [], []

    def visit(self, url: str) -> None:
        self.history.append(self.current)
        self.current = url
        self.future = []

    def back(self, steps: int) -> str:
        while self.history and steps > 0:
            self.future.append(self.current)
            self.current = self.history.pop()
            steps -= 1
        return self.current

    def forward(self, steps: int) -> str:
        while self.future and steps > 0:
            self.history.append(self.current)
            self.current = self.future.pop()
            steps -= 1
        return self.current

class BrowserHistory:
    # dynamic array
    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.cur, self.last = 0, 0 # keep track of the boundary

    def visit(self, url: str) -> None:
        self.cur += 1
        # overwrite, clear up all the forward history
        if len(self.urls) > self.cur:
            self.urls[self.cur] = url
        else:
            self.urls.append(url)   
        self.last = self.cur        

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.urls[self.cur]        

    def forward(self, steps: int) -> str:
        self.cur = min(self.last, self.cur + steps)
        return self.urls[self.cur]




