class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])   
        merged = [intervals[0]]
        for current in intervals[1:]:
            end = merged[-1]
            if current[0] <= end[1]:

                end[1] = max(end[1],current[1])
            else:
                merged.append(current)
        return  merged      

