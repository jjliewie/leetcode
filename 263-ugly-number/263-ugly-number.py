class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n == 0: return False
        
        two, three, five = True, True, True
        
        while two or three or five:
            if n%2 == 0: n /= 2
            else: two = False
            
            if n%3 == 0: n /= 3
            else: three = False
            
            if n%5 == 0: n /= 5
            else: five = False
            
        if n == 1: return True
        return False