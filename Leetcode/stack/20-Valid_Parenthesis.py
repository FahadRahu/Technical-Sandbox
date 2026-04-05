class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize Empty Stack (Array) and
        stack = []

        # Create Hashmap of "Closer":"Opener" -->
        # Closers are keys since we can just append openers, but we have to check closers to make matches
        hashmap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        # Iterate through our input string, s
        for c in s:
            if c in hashmap: # Handle our closers
                if stack and stack[-1] == hashmap[c]: # If stack NOT empty, AND end of stack == hashmap[c]
                    stack.pop()
                else:
                    return False
            else: # Handle openers (and pretty much everything else)
                stack.append(c)
        
        # We've iterated through the input, now our stack should be empty if this worked out
        return True if not stack else False