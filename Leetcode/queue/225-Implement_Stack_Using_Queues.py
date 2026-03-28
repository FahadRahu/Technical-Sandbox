from collections import deque

class MyStack:

    # This solution might not be fair since Python let's you access the last element in a queue, which makes this easy af
    # Time Complexity: O(1) for push, pop, top, and empty
    # Space Complexity: O(n) for the queue
    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        return self.q1.append(x)

    def pop(self) -> int:
        if not self.q1:
            return "There's nothing to pop :("  # type: ignore
        return self.q1.pop() # Takes from the right

    def top(self) -> int:
        return self.q1[-1] # Takes from the far right

    def empty(self) -> bool:
        if not self.q1:
            return True
        return False

"""
Thoughts:
1. Stack is LIFO, Q is FIFO
2. No Stacks, justs Q's, soooo
3. Append to queue --> i.e. q1.append([1,2,3])
4. If pop or peek, we want 1. How?
"""

class MyStack_Option2:

    # Let's work this assuming we can't access the last element in the queue, which is more fair. 
    # We can use two queues to simulate a stack. We can push elements to one queue and when we want to pop or peek, 
    # we can transfer all elements except the last one to the other queue, and then pop or peek the last element. 
    # This way, we can maintain the LIFO order of the stack using two FIFO queues.
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        # Everything BUT the last one
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        top = self.q1.popleft()
        self.q1 = self.q2
        self.q2 = deque()
        return top


        """
        q1 = [1, 2, 3]
        q2 = []
        for range(2)
        self.q2.append(self.q1.pop()) --> q1 = [2, 3] | q2 = [1]
        Again --> q1 = [3] | q2 = [1, 2]
        End of loop
        top = self.q1.popleft() --> top = [3] | q1 = [] | q2= [1, 2]
        q1 = q2
        q2 = []
        """

    def top(self) -> int:
        # Everything BUT the last one
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        top = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1 = self.q2
        self.q2 = deque()
        return top
        """
        q1 = [1, 2, 3]
        q2 = []
        Iterate for index 0 and 1, NOT 2
        q1 = [3] | q2 = [1,2]
        Save var top --> top = [3]
        append to q2 --> q1 = [] | q2 = [1, 2, 3]
        Make q1 = q2, make q2 = []
        """
    def empty(self) -> bool:
        return not self.q1 and not self.q2

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

"""
Leetcode Problem Statement:
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
"""