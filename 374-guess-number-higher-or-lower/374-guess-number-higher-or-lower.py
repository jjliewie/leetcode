# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        start, end = 1, n
        
        while start <= end:
            
            mid = (start + end)//2
            
            reply = guess(mid)
            
            if reply == 0: return mid
            
            if reply == -1: 
                end = mid - 1
            else: 
                start = mid + 1