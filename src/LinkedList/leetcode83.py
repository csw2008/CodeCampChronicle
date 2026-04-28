# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        # 链表长度不为0
        dummy = ListNode(val=-101, next=head)
        prev = dummy
        curr = dummy.next
        isEqual = False

        while True:
            if curr is None:
                if isEqual == True:
                    prev.next = curr
                    break
                else:
                    break
            if prev.val != curr.val:
                if isEqual == True:
                    isEqual = False
                    prev.next = curr
                else:
                    prev = prev.next
                    curr = curr.next
            else:
                isEqual = True
                curr= curr.next
        return dummy.next
            