class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #perform binary search across the entire matrix
        m = len(matrix)
        n = len(matrix[0])
 
        left = 0 #very first element
        right = m * n - 1

        while left <= right:

            mid = (left + right) // 2 # at index 6. 2nd row 3rd column

            #now convert mid to row and col

            midRow = mid // n
            midCol = mid % n 

            element = matrix[midRow][midCol]

            if element == target:
                return True
            
            if element < target:
                left = mid + 1
            
            else:
                right = mid - 1
    

        return False

            

