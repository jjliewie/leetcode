class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = [ch for ch in jewels]
        s = [ch for ch in stones]
        cnt = 0
        for i in s:
            for k in j:
                if k == i:
                    cnt += 1
                    break
        return cnt