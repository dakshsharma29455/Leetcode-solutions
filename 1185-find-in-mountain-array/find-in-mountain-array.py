# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        low = 1
        high = n-1
        peak = 0
        while low <= high:
            mid = low + (high - low) // 2
            mid_val = mountainArr.get(mid)
            next_val = mountainArr.get(mid + 1)
            if mid_val < next_val:
                low = mid + 1
            else:
                peak = mid         
                high = mid - 1
        low = 0
        high = peak
        while low <= high:
            mid = low + (high - low) // 2
            val = mountainArr.get(mid)
            
            if val == target:
                return mid
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
        low = peak + 1
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            val = mountainArr.get(mid)
            
            if val == target:
                return mid
            elif val > target:    
                
                low = mid + 1
            else:
                high = mid - 1 
        return -1                           

        