import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1, dict2 = dict.fromkeys(string.ascii_lowercase, 0), dict.fromkeys(string.ascii_lowercase, 0)

        for i in s:
            dict1[i] += 1
        for i in t:
            dict2[i] += 1
        if dict1 == dict2: return True
        return False
        