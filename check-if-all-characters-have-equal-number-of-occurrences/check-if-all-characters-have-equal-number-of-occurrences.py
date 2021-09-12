class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        for i in range(len(s)-1):
            if s.count(s[i]) != s.count(s[i+1]):
                return False
        return True