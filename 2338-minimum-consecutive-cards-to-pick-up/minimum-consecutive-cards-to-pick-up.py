class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        min_length = float('inf')
        seen = set()
        start = 0
        for end in range(len(cards)):
            while cards[end] in seen:
                min_length = min(min_length,end-start+1)
                seen.remove(cards[start])
                start += 1
            seen.add(cards[end])
        return min_length if min_length != float("inf") else -1        




        