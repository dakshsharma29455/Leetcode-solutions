class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        # Fill initial counts for s1 and the first window of s2
        for i in range(len1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        # Slide the window across s2
        for i in range(len2 - len1):
            if s1_counts == s2_counts:
                return True
            
            # Slide window: remove leftmost char, add next right char
            s2_counts[ord(s2[i]) - ord('a')] -= 1
            s2_counts[ord(s2[i + len1]) - ord('a')] += 1

        return s1_counts == s2_counts
        