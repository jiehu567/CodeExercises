# zip two list with O(1) space
class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Program:
    def makeAList(self, array):
        head = ListNode()
        for i in range(len(array)-1, -1, -1):
            node = ListNode(array[i])
            node.next = head.next
            head.next = node
        return head.next
    
    def printLst(self, lst):
        head = lst
        s = ""
        while head:
            s += str(head.val) + "->"
            head = head.next
        s += "null"
        print(s)
        
    def zipLists(self, lst1, lst2):
        head = ListNode()
        res = head
        p, q = lst1, lst2
        while p and q:
            if p.val < q.val:
                head.next = p
                p = p.next
            else:
                head.next = q
                q = q.next
            head = head.next
        head.next = p if p else q
        return res.next

# Test
p = Program()
lst1 = p.makeAList([3, 4, 6, 8, 9])
lst2 = p.makeAList([1, 2, 5, 7, 8, 11, 13])
lst = p.zipLists(lst1, lst2)
p.printLst(lst)
## output: 1->2->3->4->5->6->7->8->8->9->11->13->null