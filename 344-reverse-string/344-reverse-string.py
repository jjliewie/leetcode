class Solution(object):
    def reverseString(self, s):
         for i in range(len(s)//2): 
                s[i], s[-i-1] = s[-i-1], s[i]