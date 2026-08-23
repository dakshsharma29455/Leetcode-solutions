class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        Rmax = -1
        for i in range(len(arr)-1,-1,-1):
            newMax = max(Rmax, arr[i])
            arr[i] = Rmax
            Rmax = newMax
        return arr    
        