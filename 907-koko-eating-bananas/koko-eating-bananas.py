class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l,r = 1,max(piles)
        ans = r 
        while l <= r:
            k = l+(r-l) // 2
            total_hour = sum(math.ceil(p/k) for p in piles)
            if total_hour <= h:
                ans = k
                r = k-1
            else:

                l=k+1
        return ans            

        