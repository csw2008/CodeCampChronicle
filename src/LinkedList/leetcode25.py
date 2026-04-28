# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        now = dummy
        kafternode = self.getKAfter(now, k)
        while kafternode is not None:
            # 还有足够k个节点可以被交换

            # # 反转一整个链表的代码：
            # prev, curr = None, head
            # while curr:
            #     curr.next, prev, curr = prev, curr, curr.next
            # return prev

            final = kafternode.next
            prev, curr = final, now.next
            while curr != final:
                curr.next, prev, curr = prev, curr, curr.next
            curr = now.next
            now.next = prev
            now = curr
            kafternode = self.getKAfter(now, k)
        return dummy.next

    def getKAfter(self, node: ListNode, k: int) -> Optional[ListNode]:
        # 找到当前节点的第k个后面的节点
        curr = node
        while k > 0:
            curr = curr.next
            k -= 1
            if curr is None:
                return None
        return curr
