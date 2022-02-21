"""
Note that we have to keep track of nodes already processed because, as pointed out earlier, we can have cycles because of the random pointers.
    
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        old2new = {}
        cur0 = head
        cur1 = prehead1 = Node("0")
        # copy main linkedlist and add a projection
        # c0 for old list, c1 for new list
        while cur0 != None:
            n = Node(cur0.val)
            cur1.next = n
            old2new[cur0] = n
            cur1 = cur1.next
            cur0 = cur0.next
        cur0, cur1 = head, prehead1.next
        # copy random
        while cur0 != None:
            if cur0.random != None:
                cur1.random = old2new[cur0.random]
                #old2new[c0].random = old2new[c0.random]
            cur0, cur1 = cur0.next, cur1.next
        return prehead1.next


class Solution:
    def __init__(self):
        self.visited = {}
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        if head in self.visited:
            return self.visited[head]
        
        node = Node(head.val, None, None)
        self.visited[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node
        
if __name__ == '__main__':
    s = Solution()
    print(s.copyRandomList([[7,null],[13,0],[11,4],[10,2],[1,0]]))