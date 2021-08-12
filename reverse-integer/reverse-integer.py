import math

class Solution:
    def reverse(self, x: int) -> int:
        
        negative = False
        if str(x)[0] == '-':
            x = str(x)[1:]
            negative = True
        
        result = int(str(x)[::-1])
        
        if negative:
            result *= -1
        
        if result < ((math.pow(2, 31)*-1)) or result > (math.pow(2, 31)):
            return 0
        
        return result