class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        if len(s)== len(set(s)):
            return len(s)
        if len(s) == 2:
            return 1
        start, end = 0, 0
        use = {}
        for idx, value in enumerate(s):
            if value in use.keys():
                start = max(start, use[value]+1)
            end = max(end, idx+1 - start)
            use[value] = idx
        return end