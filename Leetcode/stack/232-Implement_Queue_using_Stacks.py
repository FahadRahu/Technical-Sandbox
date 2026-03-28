class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        return self.s1.append(x)

    def pop(self) -> int:
        if self.s2:
            return self.s2.pop()
        # If s2 is empty, pull from s1, if s1 empty, return none
        elif self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        else:
            return "You popped when both stacks are empty @pop func" # type: ignore

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        # If s2 is empty, pull from s1, if s1 empty, return none
        elif self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2[-1]
        else:
            return "Both stacks are empty - @peek func" # type: ignore

    def empty(self) -> bool:
        if not self.s1 and not self.s2:
            return True
        return False
        

"""
Thoughts:
1. 1 stack intake, 1 outake
"""

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()