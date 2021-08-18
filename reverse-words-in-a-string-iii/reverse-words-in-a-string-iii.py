class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        k = s.split()
        for i in range(len(k)):
            if i!= 0:
                result += ' '
            result += k[i][::-1]
        return result