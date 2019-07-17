# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode(None)
#         res = dummy
#         out, carry = 0, 0
#         while l1 or l2 or carry:
            
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0
#             carry, out = divmod(v1 + v2 + carry, 10)
#             dummy.next = ListNode(out)
#             dummy = dummy.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return res.next
            
            
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        
        carry = 0
        head = l1
        tail = l1
        
        while l1 is not None and l2 is not None:
            tmp = l1.val + l2.val + carry
            val =  tmp % 10
            carry = tmp // 10
            l1.val = val
            tail = l1
            l1 = l1.next
            l2 = l2.next
        
        while l2 is not None:
            tail.next = l2
            tmp = l2.val + carry
            l2.val = tmp % 10
            carry = tmp // 10
            tail = tail.next
            l2 = l2.next
        
        while l1 is not None:
            tmp = l1.val + carry
            l1.val = tmp % 10
            carry = tmp // 10
            tail = l1
            l1 = l1.next
            
        if carry != 0:
            tail.next = ListNode(carry)
        return head
            