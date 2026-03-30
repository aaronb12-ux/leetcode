class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        last = m + n - 1

        while m > 0 and n > 0: #loop until one of them is fully merged.

            if nums1[m - 1] < nums2[n - 1]:

                nums1[last] = nums2[n - 1]

                n -= 1
                    
            elif nums1[m - 1] > nums2[n - 1]:

                nums1[last] = nums1[m - 1]
  
                m -= 1
            
            else:

                nums1[last] = nums2[n - 1]

                n -= 1
                
            last -= 1
        

        while n > 0:

            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
        
        return nums1


        #by the end of the for loop only one of the inputs will be exhausted

        return nums1






        





