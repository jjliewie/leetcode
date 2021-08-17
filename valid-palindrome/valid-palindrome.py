class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        add = ''
        for i in s:
            if i.isnumeric() or i.isalpha():
                add += i.lower()
        return add[::-1]==add