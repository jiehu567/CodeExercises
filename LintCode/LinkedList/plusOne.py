
# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        dummy = ListNode(0)
        dummy.next = head
        
        l, r = dummy, dummy
        while r.next:
            r = r.next
            if r.val != 9:
                l = r
        
        start = l.next
        while start:
            start.val = 0
            start = start.next

        
        l.val += 1
        if dummy.val != 0:
            return dummy
        return dummy.next
        