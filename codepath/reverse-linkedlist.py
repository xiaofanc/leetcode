class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '%s -> %s' % (self.val, self.next or None)


class Solution:
	def reverseNodes(self, head):
		prev = None
		cur = head
		while cur:
			nextnode = cur.next
			cur.next = prev 
			prev, cur = cur, nextnode
		return prev

	def reverseNodes(self, head):
		if not head:
			return []
		return self.reverseNodes(head.next) + [head.val]

if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    s = Solution()
    print(s.reverseNodes(a))