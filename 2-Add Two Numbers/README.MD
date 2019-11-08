# Question
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

Output: 7 -> 0 -> 8

Explanation: 342 + 465 = 807.

# 想法
* 先求出两个数，遍历链表，按照个位，十位...进行相加即可得到。之后两个数相加得到结果的字符串形式，然后构造一个链表即可。结果用时击败99.84%，存储空间击败100%，很开心 \^_\^

    ```python
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
            
            
    ```