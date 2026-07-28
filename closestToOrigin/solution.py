from heapq import *
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        '''
            k closest -> heap algorithm

            because we want the closest, we can use a max heap


            loop through the points and calculate the distance from 0,0 and the points.

            then stores into heap the distance and points so: (0, (x,y))

            and when the length of the heap goes over k pop from it

        '''

        heap = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = math.sqrt(x ** 2 + y ** 2)

            heappush(heap, (-distance, (x, y)))

            if len(heap) > k:
                heappop(heap)
        
        return [pair[1] for pair in heap]
