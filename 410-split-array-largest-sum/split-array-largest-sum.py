class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l,r = max(nums),sum(nums)
        ans = max(nums)
        while l <= r:
            mid = l+(r-l)//2
            current_sum = 0
            subarrays = 1
            
            for num in nums:
                if current_sum + num > mid:
                    subarrays += 1
                    current_sum = num
                else:
                    current_sum += num
            if subarrays <= k:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans            



        