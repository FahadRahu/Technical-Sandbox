from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev # This means the current node now points to the prev
            prev = curr
            curr = nxt
        return prev
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if head is None or only one node, return head
        if not head or not head.next:
            return head
        
        # Recursive case: reverse the rest of the list
        new_head = self.reverseListRecursive(head.next)
        
        # Make the next node point to the current node
        head.next.next = head
        head.next = None
        
        return new_head