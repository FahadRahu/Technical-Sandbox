# The answer is to use two stacks: one to store all the elements 
# and another to store the minimum elements.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If the minStack is empty or the current value is less than or 
        # equal to the top of the minStack, push it onto the minStack as 
        # the new minimum.
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None # type: ignore

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return None # type: ignore


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()