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
    
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur.next: # type: ignore # While cur.next is a valid value
            temp = cur.next # Saves the real og cur.next
            cur.next = prev # type: ignore # changes the pointer of .next to prev
            prev = cur # moves prev to cur
            cur = temp # moves cur to the next node in the original list

        return prev # we return prev because at the end of the loop, cur will be None, and prev will be the last node in the original list, which is the new head of the reversed list
    

    """
    Thoughts:
    1 --> 2 --> 3 --> 4 --> 5
    we want
    5 --> 4 --> 3 --> 2 --> 1

    - If we start with head = 1, and the .next connection. How do we get to the end?
    - What order do we want to do things?
    - We can only start at head, and in one direction.
    - The only going in one direction is killer here
    - So, let's progress through the linked list, and each iteration, switch the pointer

    $ while cur.next # Checks if the next pointer is a value
    # How do we start with 1, point 1.next to None, and then go to 2?
    """