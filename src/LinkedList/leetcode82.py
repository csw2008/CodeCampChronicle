# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode(val=-101, next=head)
        prev, curr = dummy, dummy.next
        preprev = prev
        equal: bool = False
        while True:
            if curr is None:
                if equal == True:
                    preprev.next = None
                    break
                else:
                    break
            if prev.val != curr.val:
                if equal == False:
                    preprev = prev
                    prev = curr
                    curr = curr.next
                else:
                    equal = False
                    preprev.next = curr
                    prev = preprev 
            elif prev.val == curr.val:
                equal = True
                curr = curr.next
        return dummy.next
                