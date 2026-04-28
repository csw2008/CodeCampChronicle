# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        curr = dummy
        prev = dummy

        while curr.next is not None and curr.next.next is not None:
            slow = curr.next
            fast = curr.next.next
            prev.next = fast
            slow.next = fast.next
            fast.next = slow
            prev = slow
            curr = slow
        return dummy.next