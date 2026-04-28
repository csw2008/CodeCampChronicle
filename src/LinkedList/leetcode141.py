# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针固定套路，记住
        # 空间O(1)
        if head is None:
            return None
        slow, fast = head, head
        while True:
            if fast.next is None or fast.next.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                fast = head
                return True
        