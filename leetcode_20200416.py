leetcode 20200416

Q3: delete duplicate nodes from a sorted linkedlist
Example:
input: 1 -> 1 -> 2 -> 3 -> 3 -> null
output: 1 -> 2 -> 3

In general, in order to make .next meaningful
def dedup(head):
    if not head or not head.next: return 
    prev, cur = head, head.next
    while cur:
        if cur.value != prev.value:
            prev.next = cur
            prev = prev.next
        cur = cur.next
    return head 
