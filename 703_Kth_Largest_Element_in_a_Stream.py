import heapq
from heapq import heappush, heappop, heapify
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        heapify(self.heap)
        for num in nums:
            heappush(self.heap, num)
        
        while self.k < len(self.heap):
            heappop(self.heap)

    def add(self, val: int) -> int:
        if self.heap and val < self.heap[0]:
            if self.k > len(self.heap):
                heappush(self.heap, val)
                return self.heap[0]
            return self.heap[0]
        else:
            heappush(self.heap, val)
            if self.k < len(self.heap):
                heappop(self.heap)
            return self.heap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(2,[0])
param_1 = obj.add(-1)
print(param_1)