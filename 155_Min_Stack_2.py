
from heapq import heappush, heappop, heapify
class MinStack:

    def __init__(self):
        self.Stack = []
        self.minStack = []
        heapify(self.minStack)
    def push(self, val: int) -> None:
        self.Stack.append(val)
        heappush(self.minStack, val)

    def pop(self) -> None:
        popE = self.Stack.pop()
        # if popE not in self.Stack and popE in self.minStack:
        #     heappop(self.minStack)

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        while self.minStack[0] not in self.Stack:
            heappop(self.minStack)
        return self.minStack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()