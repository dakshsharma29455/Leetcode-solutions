class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count = 0
        for i in range(len(s) - k + 1):
            sub_num = int(s[i:i+k])
            if sub_num != 0 and num % sub_num == 0:
                count += 1
        return count        