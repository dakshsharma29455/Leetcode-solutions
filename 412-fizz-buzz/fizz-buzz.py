class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1,n+1):
            if i % 15 == 0:
                ans = "FizzBuzz"
            elif i % 3 == 0:
                ans = "Fizz"
                
            elif i % 5 == 0:
                ans = "Buzz"
            else:
                ans = str(i)
            output.append(ans)     
        return output                   