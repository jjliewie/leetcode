import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        
        if x == 0:
            return True
        
        if x < 0:
            return False
        
        for i in range(math.floor(len(number)/2)):
            if number[i] != number[len(number)-i-1]:
                return False
        
        return True