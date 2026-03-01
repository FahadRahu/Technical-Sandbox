from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map: dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res: List[str] = []
        
        # Index = the current position in the digits string that we are processing
        # Path = the current combination of letters being formed
        def backtrack(index: int, path: str):
            if index == len(digits):
                res.append(path)
                return
            
            # iterate over the letters that the current digit maps to
            for char in phone_map[digits[index]]:
                backtrack(index + 1, path + char)

        backtrack(0, "")
        return res
    

"""
An example of this would look like: 
if digits = "23", the function would generate ["ad","ae","af","bd","be","bf","cd","ce","cf"] 

An iteration step by step would look like: 
1. Start with an empty path and index 0.
2. For the first digit '2', iterate over 'a', 'b', 'c'.
3. For each letter, move to the next digit '3' and iterate over 'd', 'e', 'f'.
4. Combine each letter from the first digit with each letter from the second digit to form the combinations.
5. Append each complete combination to the result list.

backtrack(0, "")
├─ For char 'a' in phone_map["2"]:
│  └─ backtrack(1, "a")
│     ├─ For char 'd' in phone_map["3"]:
│     │  └─ backtrack(2, "ad")
│     │     └─ Reached end (index=2==len("23"))
│     │        └─ Append "ad" to results ✓
│     ├─ For char 'e' in phone_map["3"]:
│     │  └─ backtrack(2, "ae")
│     │     └─ Append "ae" to results ✓
│     └─ For char 'f' in phone_map["3"]:
│        └─ backtrack(2, "af")
│           └─ Append "af" to results ✓
├─ For char 'b' in phone_map["2"]:
│  └─ backtrack(1, "b")
│     ├─ backtrack(2, "bd") → Append "bd" ✓
│     ├─ backtrack(2, "be") → Append "be" ✓
│     └─ backtrack(2, "bf") → Append "bf" ✓
└─ For char 'c' in phone_map["2"]:
   └─ backtrack(1, "c")
      ├─ backtrack(2, "cd") → Append "cd" ✓
      ├─ backtrack(2, "ce") → Append "ce" ✓
      └─ backtrack(2, "cf") → Append "cf" ✓


The Algorithm In Plain English
1. Start with digit at position 0 and empty string
2. For each letter that digit maps to:
3. Add that letter to the current path
4. Move to the next digit
5. Repeat step 2 with the next digit
6. When you've used all digits, you have a complete combination
7. Save it and "backtrack" to try other letters
            
"""