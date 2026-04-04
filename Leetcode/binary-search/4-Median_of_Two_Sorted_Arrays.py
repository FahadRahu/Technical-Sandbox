class Solution:
    # Time complexity: O(log(min(m,n))) where m and n are the lengths of the two arrays. We perform a binary search on the smaller array.
    # Space complexity: O(1) since we are using only a constant amount of extra space.
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A): # Ensure A is the smaller array
            A, B = B, A 
        
        l, r = 0 , len(A) - 1 # Binary search on the smaller array
        while True: # Infinite loop, will break when median is found
            i = (l + r) // 2 # A's middle index
            j = half - i - 2 # B's middle index, subtract 2 for 0-based index

            # We add the condition because we want to make sure that we are not out of bounds when we access A[i] and B[j]
            Aleft = A[i] if i >= 0 else float("-infinity") # If i is out of bounds, use -infinity
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity") # If i + 1 is out of bounds, use infinity
            Bleft = B[j] if j >= 0 else float("-infinity") # If j is out of bounds, use -infinity
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity") # If j + 1 is out of bounds, use infinity

            # Partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # If total length is odd, return the middle element
                if total % 2:
                    return min(Aright, Bright)
                # If total length is even, return the average of the two middle elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: # We are too far on the right side for partition A. Go left.
                r = i - 1
            else: # We are too far on the left side for partition A. Go right.
                l = i + 1