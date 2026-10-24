class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findBound(isFirst: bool) -> int:
        
            low, high = 0, len(nums) - 1
            bound = -1
            while low <= high:
                mid = low +(high - low)//2
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        high = mid - 1
                    else:
                        low = mid  + 1    
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return bound 
        first = findBound(isFirst=True)
        if first == -1:
            return [-1, -1]
        last = findBound(isFirst=False)
        return [first, last]    
              

        