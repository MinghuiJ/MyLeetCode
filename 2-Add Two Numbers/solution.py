# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, k1 = 0, 1
        num2, k2 = 0, 1
        h1 = l1
        h2 = l2
        while h1!=None:
            num1 += h1.val * k1
            k1 *= 10
            h1 = h1.next
        while h2!=None:
            num2 += h2.val * k2
            k2 *= 10
            h2 = h2.next
        res = str(num1 + num2)
        ret = ListNode(res[-1])
        p = ret
        for i in range(len(res)-2, -1, -1):
            node = ListNode(res[i])
            p.next = node
            p = p.next
        return ret
        
        