'''
Example 2: You are given a binary string s (a string containing only "0" and "1"). 
You may choose up to one "0" and flip it to a "1". 
What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. 
If you perform the flip at index 2, the string becomes 1111100111.
'''

'''
This problem is basically asking whats the longest substring of all 1's and 1 zero

 
 
"1 1 0 1 1 0 0 1 1 1" 

'''

def longestSubFlip0(nums):


    leftPtr = 0
    ans = 0
    currentZeros = 0

    for rightPtr in range(len(nums)):
 
        if nums[rightPtr] == "0":
            currentZeros += 1
        
        while currentZeros > 1:

            if nums[leftPtr] == "0":
                currentZeros -= 1
            
            leftPtr += 1
    

        ans = max(ans, rightPtr - leftPtr + 1)
    
    return ans
