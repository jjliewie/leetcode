class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tl = [w for w in t]
        for i in s:
            if i not in tl:
                return False
            tl = tl[tl.index(i)+1:]
        return True