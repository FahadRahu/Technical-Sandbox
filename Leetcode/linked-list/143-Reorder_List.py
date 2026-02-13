from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time Complexity: O(n) | Space Complexity: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # We don't need this since LC guarantees it's not empty, 
        # I'm just doing it so VSCode errors shut up
        if not head:
            return None
        
        # Three main steps:
            # 1. Find the middle of the linked list to split half/half  (if odd, the extra with 1st half)
            # 2. Change the direction of the second linked list to point the opposite way
            # 3. Merge the two arrays (hardest part imo)
        
        
    # First, split the linked list in two using slow & fast pointers to get the middle
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next # type: ignore
            fast = fast.next.next

        # Great, that takes care of finding the middle.
        # Slow will be the end of the first list, slow.next is the start of the next list
        

        # Start of Second List is slow.next
        second = slow.next # type: ignore


    # Second, change the direction of the pointers of the 2nd list to point the opposite way
        # Point slow.next to None to split the 1st and 2nd list. 
        # Set a new var, prev, to None to prep for next step - switch the directions
        prev = slow.next = None # type: ignore
        
        # The strategy for this step is:
            # 1. Set a temp var to second.next
            # 2. Point second.next to prev
            # 3. Set prev to second
            # 4. Set second to tmp
            # 5. Repeat the loop until second becomes None, meaning prev is the "last" (now first) value
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Great, that takes care of switching the pointers. 
        # The last value has become the head of the 2nd linked list. 
        # Since second went to None, prev is last valid value, and the new head of the 2nd linked list
    

    # Third, merge the two lists
        # Set first to the head of the 1st list, set second to the head of the 2nd list
        first, second = head, prev

        # Strategy:
            # Since we KNOW the linked list is either evenly split, OR the extra value is with the 1st list,
            # we can keep going until the second becomes invalid.
        while second:
            
            # 1. Save first.next and second.next as tmp1 and tmp2 vars respectively
            # 2. Point first.next to second
            # 3. Point second.next to tmp1
            # 4. Set first to tmp1
            # 5. Set second to tmp2

            tmp1 = first.next # type: ignore
            tmp2 = second.next
            first.next = second # type: ignore
            second.next = tmp1
            first = tmp1
            second = tmp2
