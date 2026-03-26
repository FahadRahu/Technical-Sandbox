from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            else: # Stack has stuff in it
                while temperatures[i] > temperatures[stack[-1]] and stack:
                    res[stack[-1]] = i - stack[-1]  # Update res[top_of_stack]
                    stack.pop()
                stack.append(i)
        return res
    
    def dailyTemperaturesAlternate(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]  # Update res[top_of_stack]
                stack.pop()
            stack.append(i)
        return res
    
    def dailyTemperaturesNeetcode(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures): # Gives us index and value in that order
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop() # Get the value and index of the top of the stack
                res[stackInd] = i - stackInd # Update res[top_of_stack_index]
            stack.append((t, i))
        return res