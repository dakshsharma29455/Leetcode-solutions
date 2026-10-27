class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        gains = sorted(
            [int(''.join(sorted(str(x),reverse=True))) - x for x in nums],
            reverse=True
        )
        return sum(nums) + sum(gains[:k])
        
            
        