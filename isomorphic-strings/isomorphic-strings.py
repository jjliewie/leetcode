class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def number(string):
            counter = 0
            dic = {}
            for i in string:
                dic[i] = counter
                counter += 1
            result = ""
            for i in string:
                result += str(dic[i])
            return result
        
        if number(s) == number(t):
            return True
        return False