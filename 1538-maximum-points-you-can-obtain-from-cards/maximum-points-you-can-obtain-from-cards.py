class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        L_sum = 0
        R_sum = 0
        max_sum = 0
        for i in range(k):
            L_sum += cardPoints[i]
            max_sum = L_sum
            R_ind = n-1
        for i in range(k-1,-1,-1):
            L_sum -= cardPoints[i]
            R_sum += cardPoints[R_ind]
            R_ind = R_ind -1
            max_sum = max(max_sum,L_sum + R_sum)
            
        return max_sum        

        
            
        