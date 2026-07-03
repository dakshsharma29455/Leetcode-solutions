class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_hash = {}
        n = len(s)
        l = 0
        r = 0
        max_len = 0
        while r < n:
            if s[r] in char_hash:
                if char_hash[s[r]] >= l:
                    l = char_hash[s[r]] + 1 
            new_len = r - l + 1
            max_len = max(new_len,max_len)
            char_hash[s[r]] = r
            r += 1
        return max_len                                

            
            

        