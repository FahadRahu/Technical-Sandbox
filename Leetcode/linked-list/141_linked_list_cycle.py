# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow, fast = head, head

        # We don't need slow since it WILL be slow. I just want the type error to not happen in slow.next.
        while fast and fast.next and slow: # fast.next because if fast.next is None, fast.next.next will raise an error
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False