class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = [w for w in magazine]
        for i in ransomNote:
            if i not in mag:
                return False
            mag.remove(i)
        return True