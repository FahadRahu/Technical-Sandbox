from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        tail = dummy

        # While both lists have nodes to compare
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # Append list1's node to merged list
                list1 = list1.next  # Move to the next node in list1
            else:
                tail.next = list2  # Append list2's node to merged list
                list2 = list2.next  # Move to the next node in list2
            tail = tail.next  # Move the tail pointer

        # If there are remaining nodes in either list, append them
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next  # Return the merged list, skipping the dummy node

def practicing_using_a_linked_list():
    # Creating two sorted linked lists for testing
    a = ListNode(1, ListNode(2, ListNode(4, ListNode(6))))
    b = ListNode(1, ListNode(3, ListNode(4, ListNode(5))))
    print("List A:")
    curr = a
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("The end")
    print("List B:")
    curr = b
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("The end")

print("Practicing linked list creation and traversal:")
practicing_using_a_linked_list()

# My original thought process
# 1. Make a list 3
# 2. Start from list 1 and list 2
# 3  Compare the first of each
# 4. Put the smaller one in list 3
# 5. Move chosen list's pointer up by one.
# 6. Compare again
# 7. Repeat step 4 and 5 until at the end of one list
# 8. Throw the rest of the remainder list into list 3

# What I learned from the solution
# 1. Use a dummy node to start the merged list - it gives a starting point to attach nodes.
# 2. Use a tail pointer to keep track of the end of the merged list.
# 3. Efficiently handle remaining nodes by directly attaching them once one list is exhausted.
# 4. The final merged list is obtained by returning dummy.next, skipping the dummy node itself.