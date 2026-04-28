"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        # dummy = Node(x=-10001, next=head, random=None)
        # dummyPrime = Node(x=-10001, next=head, random=None)
        # dummy.next = dummyPrime

        curr = head
        while curr is not None:
            currPrime = Node(x=curr.val, next=curr.next, random=None)
            curr.next = currPrime
            curr = curr.next.next
        curr = head
        headPrime = head.next
        while curr is not None: # 只处理random指针
            currNext = curr.next.next
            currPrime = curr.next
            currPrime.random = curr.random.next if curr.random else None
            curr = currNext
        curr = head
        while curr is not None: # 恢复原链表
            currPrime = curr.next
            currNext = curr.next.next
            curr.next = currNext
            currPrime.next = currNext.next if currNext else None
            curr = currNext

        return headPrime
