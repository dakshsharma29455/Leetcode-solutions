class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        if len(dist) > math.ceil(hour):
            return -1
        l,r = 1,10**7
        ans = -l
        while l <= r:
            mid = l+(r-l)//2
            total_time = 0.0
            for i in range(len(dist)-1):

                total_time += math.ceil(dist[i]/mid)
            total_time += dist[-1]/mid
            if total_time <= hour:
                ans = mid
                r = mid -1
            else:
                l = mid +1
        return ans         



        