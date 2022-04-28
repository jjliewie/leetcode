class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tl = [w for w in t]
        for i in s: tl.remove(i) 
        return tl[0]
            