# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head) # 虚拟头节点
        slow = dummy
        fast = dummy
        # 倒数第n个和正数第n个本质上只有从哪边数的区别
        for i in range(n):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
        