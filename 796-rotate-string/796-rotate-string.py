class Solution:
    
    def shift(self, s: str):
        return s[1:] + s[:1]
        
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            s = self.shift(s)
            if s == goal:
                return True
        return False