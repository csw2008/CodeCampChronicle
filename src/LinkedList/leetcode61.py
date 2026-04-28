# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        Len = self.getLen(head)
        if Len == 0:
            return None
        k = k % Len

        dummy = ListNode(val=0, next=head)
        curr = dummy
        while curr.next is not None:
            curr = curr.next
        
        last = curr
        curr = dummy
        for i in range(Len - k):
            curr = curr.next
        last.next = dummy.next
        dummy.next = curr.next
        curr.next = None
        return dummy.next


    
    def getLen(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(val=0, next=head)
        l = 0
        while dummy.next is not None:
            dummy = dummy.next
            l += 1

        return l