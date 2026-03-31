'''
Example 4: Given an integer array nums and 
an integer k, find the sum of the subarray with the largest sum whose length is k.
'''
        

'''
    input: 
        nums: array of ints
        k: length of subarrays

    output:
        greatest sum subarray of length k in nums

'''


def greatestSumK(nums, k):

    
    ans = 0
    currentWindow = 0
    leftPtr = 0

    for rightPtr in range(k): #builds the first window
        currentWindow += nums[rightPtr]
    

    ans = currentWindow
    for rightPtr in range(k, len(nums)): 

        currentWindow = currentWindow + nums[rightPtr] - nums[leftPtr]
        leftPtr += 1

        ans = max(ans, currentWindow)
    
    return ans
