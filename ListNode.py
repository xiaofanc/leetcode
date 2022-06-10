class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __str__(self):
        return '%s->%s' % (self.val, self.next or '')

    def __gt__(self, other):
        return True

    def __lt__(self, other):
        return False

    @classmethod
    def from_list(cls, nums):
        if nums == []: return None
        else: return cls(nums[0], cls.from_list(nums[1:]))


if __name__ == '__main__':
    l1=ListNode.from_list([1,2,3,4,5])
    l2=ListNode.from_list([1,2])
    l3=ListNode.from_list([1])
    print(l1)