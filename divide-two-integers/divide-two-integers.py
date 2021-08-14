class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = dividend/divisor
        
        if str(a).index('.') != 0:
            a = int(str(a)[:str(a).index('.')])
            
        if a > (2**31 -1):
            return 2**31 -1
        if a < (-2**31):
            return -2**31
        
        return a