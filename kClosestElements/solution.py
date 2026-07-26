from heapq import *
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
            convert into heap ? -> while greater than 

            [1, 2, 3, 4, 5] k = 4, x = 3

            iterate over arry and add to heap and pop when we exceed size k

            keep a max heap because we want to pop the greater values

            [0,0,1,2,3,3,4,7,7,8] k = 3 x = 5

            heap = [-1, 0, 0]

            1
        
        #build the heap based off distance
        #then build an array of the k smallest elements in the heap


        [0,0,1,2,3,3,4,7,7,8] k = 3 x = 5
                         X
      

  
 ``
        heap =(-2, -3), (-2, -3), (-1, -4)
        ''' 
 
        heap = []

        for num in arr:

            distance = abs(x - num)

            heappush(heap, (-distance, -num)) #pushing onto the 

            if len(heap) > k:
                heappop(heap)
            
        return sorted([-pair[1] for pair in heap])
        
