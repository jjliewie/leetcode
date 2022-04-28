class Solution:
    def longestPalindrome(self, s: str) -> int:
        d, ans = {}, 0
        for i in s:
            if i in d.keys():
                d[i] += 1
            else: d[i] = 1
        for v in d.values():
            ans += (v//2)*2
        return min(ans+1, len(s))