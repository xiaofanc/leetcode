# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '[%s, %s]' % (self.val, self.next or '')

class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        dummy = prev = ListNode(0)
        s, f = head, head.next
        while f:
            if s.val != f.val:
                prev.next = s
                prev = prev.next      # move to the next position
                s = s.next
                f = f.next
            else: # s.val = f.val, move f to the next different value
                while f.next and f.val == f.next.val:
                    f = f.next
                if not f.next:
                    prev.next = None  # mark the end
                    return dummy.next
                else:
                    # f is the first different value
                    s = f.next
                    f = f.next.next
        prev.next = s
        return dummy.next

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # sentinel
        sentinel = ListNode(0, head)

        # predecessor = the last node 
        # before the sublist of duplicates
        pred = sentinel
        
        while head:
            # if it's a beginning of duplicates sublist 
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                pred.next = head.next 
                # print("pred, ", pred.val)
                # print("pred.next, ", pred.next.val)
            # otherwise, move predecessor
            else:
                pred = pred.next 
                
            # move forward
            head = head.next
            
        return sentinel.next

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        if head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
            
if __name__ == '__main__':
    L = ListNode
    head = L(1)
    head.next = L(2)
    head.next.next = L(2)
    s = Solution()
    print(s.deleteDuplicates(head))  # [1]


