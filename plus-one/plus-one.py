class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        k = int(''.join([str(i) for i in digits]))
        k +=1
        k = [int(j) for j in str(k)]
        return k