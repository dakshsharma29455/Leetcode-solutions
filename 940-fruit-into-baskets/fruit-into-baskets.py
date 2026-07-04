class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        r = 0 
        l = 0
        basket = {}
        for r in range(len(fruits)):
            basket[fruits[r]] = basket.get(fruits[r], 0) + 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            new_len = r - l + 1
            max_len = max(max_len,new_len)
        return max_len            


        