nums1 = [4,1,2]
nums2 = [1,3,4,2]
nums3 = [2,1,3,4]

class Solution:
    # Time Complexity: O(n^2) - Nested Loops
    # Space Complexity: O(n) - Dictionary and Answer List
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]: 
        nums1_dict = {}
        answer = [-1] * len((nums1))
        print(f'The initialized answer list is: {answer}')

        for i, n in enumerate(nums1): # Match Key:Value as Value:Index of the nums1 list
            nums1_dict[n] = i
            print(nums1_dict)
        print('')

        for i in range(len(nums2)): # Iterate through each index i in nums2

            if nums2[i] in nums1_dict: # If there's a match - nums2[i] is a key in our dictionary

                for j in range(i+1, len(nums2)): # Iterate each index after in nums2 - see if there's a > value
                    if nums2[j] > nums2[i]: # Okay, we found a greater number! Now What?
                        
                        # We need to put nums2[j] into our answer list, BUT, specifically at the right index
                        # nums2[j] needs to go in the index where nums2[i] is in our dictionary BECAUSE
                        # nums2[i] is a key matched to it's index. nums2[i]:index (for nums1)

                        a = nums1_dict[nums2[i]] # This gives us the .value not the key for the key/item pair.
                        # a is being set to the index in the nums1 list where we see nums2[i] equals a nums1 value

                        answer[a] = nums2[j] # Now we can set the answer list at index a to nums2[j], the next greater number
                        break


        return(answer)
    
    def nextGreaterElement_optimized(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Time Complexity: O(n) - Single Pass with Stack
        # Space Complexity: O(n) - Dictionary, Answer List, and Stack
        print(f"nums1 is: {nums1}\nnums2 is: {nums2}",end="\n\n")
        nums1_indx = {n:i for i, n in enumerate(nums1)} # Dictionary Comprehension to map nums1 values to their indices
        print(f'The nums1 index mapping is: {nums1_indx}')
        answer = [-1] * len((nums1))
        print(f'The initialized answer list is: {answer}', end="\n\n")

        stack = []
        
        for i in range(len(nums2)): # Iterate through each index i in nums2
            print(f'Current Stack: {stack}')
            cur = nums2[i] # The value at the list and position nums2[i]
            while stack and cur > stack[-1]: # While stack is not empty AND current value is greater than the last value in the stack
                val = stack.pop() # Pop the last value from the stack and store it in 'val'
                indx = nums1_indx[val] # Get the index of 'val' from nums1_indx dictionary and store it in 'indx'
                answer[indx] = cur # Set the answer at index 'indx' to the current value 'cur'
            if cur in nums1_indx: # If the current value is in nums1_indx dictionary
                stack.append(cur) # Append the current value to the stack
        return answer

solution = Solution()
# a = solution.nextGreaterElement(nums1, nums2) # Using the unoptimized version
b = solution.nextGreaterElement_optimized(nums1, nums3) # Using a stack for optimization
print(b)