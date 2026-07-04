           
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        zero = 0
        l = 0
        r = 0
        max_len = 0
        while r < n:
            if nums[r] == 0:
                zero += 1
            while zero > k:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            if zero <= k:
                new_len = r - l + 1
                max_len = max(new_len,max_len)
            r += 1    
        return max_len 


        
       
        
        # Variable to store max length
        
