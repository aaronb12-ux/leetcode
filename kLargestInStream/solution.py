from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        print(self.heap)
        for i in range(len(self.heap) - k): #remove smaller extra elements
            heappop(self.heap)

    def add(self, val: int) -> int:

        heappush(self.heap, val)

        if len(self.heap) > self.k:
            heappop(self.heap)
        
        return self.heap[0]




        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

'''
we want the kth largest so we keep a min heap because all children will be greater than it
'''
