class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        start = 0
        current_sum = 0
        max_sum = float('-inf')
        for end in range(len(nums)):
            current_sum += nums[end]
            if end - start + 1 == k:
                if current_sum > max_sum:
                    max_sum = current_sum
                current_sum -= nums[start]
                start += 1
        return max_sum / k        


        