class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if abs(int(log(n, 2)) - log(n, 2)) < 0.000000001:
            return True
        return False