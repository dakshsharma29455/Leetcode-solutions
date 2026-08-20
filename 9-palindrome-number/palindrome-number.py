class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num =  x
        result = 0
        
        while(num>0):
            digit = num % 10
            result = (result*10)+digit
            num = num // 10
        
        if x == result:
            return True
        else:
            return False
                
                

        