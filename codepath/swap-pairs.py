# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '%s -> %s' % (self.val, self.next or None)


class Solution:
    # when swapping, need to keep track of the previous node of the pairs and the 
    # node after the pairs in order to connect them
    # pre must exist !!!!
    # pre -> n1 -> n2  -> tmp
    # pre -> n2 -> n1  -> tmp
                 # pre -> n1  -> n2  -> tmp
    def swapPairs(self, head):
        pre=dummy=ListNode(0)
        pre.next=head
        while pre.next and pre.next.next:
            n1 = pre.next
            n2 = n1.next
            #pre.next,n2.next,n1.next=n2,n1,n2.next
            next_node = n2.next
            pre.next = n2
            n2.next=n1
            n1.next=next_node
            pre = n1
        return dummy.next

    # does not work since losing connect from pre -> n2
    def swapPairs2(self, head):
        if not head or not head.next:
            return head
        dummy = n1 = head
        n2 = head.next
        while n1 and n2:
            tmp = n2.next
            n2.next = n1
            n1.next = tmp
            if tmp:
                n1 = tmp
                n2 = tmp.next
            print("dummy->", dummy)
        return dummy.next

    def swapPairs(self, head):
        if not head or not head.next:
            return head
        # recursion
        first_node = head
        second_node = head.next
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        
        return second_node

if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    s = Solution()
    print(s.swapPairs2(a))

# Given 1->2->3->4, you should return 2->1->4->3

# 0 -> 1 -> 2 -> 3 -> 4
# p    n1   n2 next_node
# 0 -> 2 -> 1 -> 3 -> 4
#           p    n1   n2  next_node
# 0 -> 2 -> 1 -> 4 -> 3

