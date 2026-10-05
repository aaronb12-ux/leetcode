class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        '''
            conveyer belt of packages -> one port to another within d days

            the ith package has weighit weights[i]

            each day, we load the ship with packages on the conveyerbelt. 

            we cannot load more weight than the max weight capacity (need to solve for this) on the ship

            return the least weight capacity of the ship that wi

            so we have a range

            low                         high

            need to find value in here (inclusive) that meets the expectations above

            so if our value is x

            we need to loop through the weights and for each package add it to a sum. if adding the curr package to the sum exceeds x, then we have our first shipment. we then continue with the curr package and do the same thing. if we finish this process and we are at less than or equal to days, then we check a smaller values, else, check a larger value. this involves a binary search
        '''

        left = max(weights)
        right = sum(weights)
        best = 0

        def valid_capacity(capacity):
            curr_sum = 0
            d = 1

            for weight in weights:

                if curr_sum + weight > capacity:
                    d += 1
                    curr_sum = weight
                else:
                    curr_sum += weight

            return d <= days

        
        while left <= right:
             
            middle = (left + right) // 2 #capacity

            if valid_capacity(middle):
                best = middle
                right = middle - 1

            else:
                left = middle + 1
        

        return best
            
