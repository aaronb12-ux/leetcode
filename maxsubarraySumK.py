def subarraySumK(nums, k):

      
    #           l  r
    # [3, 1, 2, 7, 4, 2, 1, 1, 5] k = 8


    leftPtr = 0
    maxWindow = 0
    currentSum = 0

    for rightPtr in range(len(nums)):

        currentSum += nums[rightPtr]

        while currentSum > k:

            currentSum -= nums[leftPtr]
            left += 1 
            
        maxWindow = max(maxWindow, rightPtr - leftPtr + 1)

    
    return maxWindow
