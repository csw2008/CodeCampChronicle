# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        now = None
        head = ListNode(val=(l1.val+l2.val)%10)
        carry = int((l1.val+l2.val)/10)
        cur1 = l1.next
        cur2 = l2.next
        now = head
        while not (cur1 is None and cur2 is None and carry == 0):

            cur1 = cur1 if cur1 is not None else ListNode()
            cur2 = cur2 if cur2 is not None else ListNode()
            # if int(cur1.val + cur2.val + carry) == 0:
            #     break
            now.next = ListNode(val=(cur1.val+cur2.val+carry)%10)
            carry = int((cur1.val+cur2.val+carry) / 10)
            cur1 = cur1.next
            cur2 = cur2.next
            now = now.next
        return head
                