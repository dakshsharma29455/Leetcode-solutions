class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        max_water = 0
        while left < right:
            width = right - left
            new_height = min(height[left] , height[right])
            new_water = width * new_height
            max_water = max(max_water,new_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water        

