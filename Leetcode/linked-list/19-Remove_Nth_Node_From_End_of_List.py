from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        if not right:
            return head.next # type: ignore
        
        while right.next:
            left = left.next # type: ignore
            right = right.next
        
        left.next = left.next.next # type: ignore

        return head
    
    def neetCodeSolution(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next # type: ignore
            right = right.next
        
        left.next = left.next.next # type: ignore

        return dummy.next