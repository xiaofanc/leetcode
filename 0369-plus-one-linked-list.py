# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # Write your code here
        if not head:
            return
        not_nine = dummy = ListNode(0)
        not_nine.next = head
        # get the rightmost not 9
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        not_nine.val += 1
        nine = not_nine.next

        # replace the remaining 9 to be 0
        while nine:
            nine.val = 0
            nine = nine.next
        return dummy if dummy.val == 1 else dummy.next

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([0]))  # [1]