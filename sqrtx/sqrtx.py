class Solution(object):
    def mySqrt(self, x):
        answer = x
        while answer*answer > x:
            answer = (answer + x/answer)/2
        
        return(answer)