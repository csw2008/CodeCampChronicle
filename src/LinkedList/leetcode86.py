# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        dummy = ListNode(val=0, next=head)
        prev, curr = dummy, dummy.next
        BH = ListNode(val=-101, next=None)
        prevBH = dummy
        while curr is not None:

            if BH.val == -101:
                # 之前没有遇到过大于等于x的节点
                if curr.val < x:
                    prev = curr
                    curr = curr.next
                else:
                    # 现在第一次遇到大于等于x的节点
                    BH = curr
                    prevBH = prev
                    prev = curr
                    curr = curr.next
            else:
                # 之前遇到过大于等于x的节点
                if curr.val >= x:
                    prev = curr
                    curr = curr.next
                else:
                    prev.next = curr.next
                    prevBH.next = curr
                    curr.next = BH
                    prevBH = curr
                    curr = prev.next
        return dummy.next
                    