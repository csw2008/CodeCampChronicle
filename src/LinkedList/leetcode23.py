# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class NodeWrapper:
            def __init__(self, listnode: ListNode):
                self.listnode = listnode
            def __lt__(self, other: ListNode):
                return self.listnode.val < other.listnode.val

        curr: List[Optional[ListNode]] = []
        for i in range(len(lists)):
            if lists[i] is not None:
                curr.append(NodeWrapper(lists[i]))

        dummy = ListNode(val=0, next=None)
        now = dummy

        import heapq
        heapq.heapify(curr)
        while curr: # 不为空
            now.next = heapq.heappop(curr).listnode
            now = now.next
            if now.next is not None:
                heapq.heappush(curr, NodeWrapper(now.next))
            
        return dummy.next

            