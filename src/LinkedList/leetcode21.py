# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: 
            return list2
        if not list2:
            return list1
        # 两个列表长度均不为0
        
        cur1 = list1
        cur2 = list2
        
        dummy = ListNode(val=0, next=None)
        curr = dummy

        # 把链表1和链表2拼接到链表dummy.next上
        while cur1 is not None and cur2 is not None:
            if cur1.val <= cur2.val:
                newnode = ListNode(val=cur1.val, next=None)
                curr.next = newnode
                curr = curr.next
                cur1 = cur1.next
            else:
                newnode = ListNode(val=cur2.val, next=None)
                curr.next = newnode
                curr = curr.next
                cur2 = cur2.next

        while cur1 is not None:
            newnode = ListNode(val=cur1.val, next=None)
            curr.next = newnode
            curr = curr.next
            cur1 = cur1.next
        while cur2 is not None:
            newnode = ListNode(val=cur2.val, next=None)
            curr.next = newnode
            curr = curr.next
            cur2 = cur2.next
        return dummy.next