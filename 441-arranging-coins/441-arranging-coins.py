class Solution:
    def arrangeCoins(self, n: int) -> int:
        tmp = 1
        while n >= tmp:
            n -= tmp
            tmp +=1
        return tmp-1