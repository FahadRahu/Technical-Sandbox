from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Reverse the integer array to make addition easier
        digits = digits[::-1]
        # Initialize carry to 1 since we are adding one to the number
        carry, i = 1, 0
        while carry:
            if i < len(digits):
                # If the current digit is 9, it will become 0 and we carry over 1 to the next digit
                if digits[i] == 9:
                    digits[i] = 0
                # If the current digit is not 9, we can simply add the carry to it and set carry to 0, this ends every addition
                else:
                    digits[i] += 1
                    carry = 0
            # If we have reached the end of the digits array and still have a carry, we need to append a new digit
            else:
                digits.append(1)
                carry = 0
            i += 1
        return digits[::-1]
    
    def alternativeSolution(self, digits: List[int]) -> List[int]:
        # Convert the list of digits to a single integer
        num = int(''.join(map(str, digits)))
        # Add one to the integer
        num += 1
        # Convert the integer back to a list of digits
        return [int(d) for d in str(num)]