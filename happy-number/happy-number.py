class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 2 or n == 3 or n == 4: 
            return False
        k = 0
        for i in str(n):
            k += int(i)**2
        return self.isHappy(k)