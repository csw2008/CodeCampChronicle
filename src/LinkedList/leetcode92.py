# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        # # 翻转整个链表的代码实现：
        # prev, curr = None, head
        # while curr:
        #     curr.next, prev, curr = prev, curr, curr.next
        # return prev

        dummy = ListNode(val=0, next=head)
        curr = dummy
        currLeft = dummy
        for i in range(left):
            currLeft = curr
            curr = curr.next
        # 此时curr在left处
        kAfterNode = self.getKafter(curr, right-left)
        final = kAfterNode.next
        
        prev, curr = final, curr
        while curr != final:
            curr.next, prev, curr = prev, curr, curr.next
        currLeft.next.next = curr
        currLeft.next = prev

        return dummy.next

        
    def getKafter(self, node: ListNode, k: int):
        # 找到node节点之后的第k个节点并返回
        while k > 0:
            node = node.next
            k -= 1
            if node is None:
                return None
        return node