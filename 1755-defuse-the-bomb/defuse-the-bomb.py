class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        result = [0]*n
        if k == 0:
            return result
        if k > 0:
            start = 1
            end = k
        else: 
            start = n + k
            end = n - 1
        window_sum = 0
        for i in range(start, end + 1):
            window_sum += code[i % n]
            
        result[0] = window_sum       
        for i in range(1,n):
            window_sum -= code[(start) % n]
            start += 1
            end += 1
            window_sum += code[(end) % n]
            
            result[i] = window_sum
        return result    