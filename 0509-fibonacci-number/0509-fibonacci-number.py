class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        a, b, ans = 0, 1, 0
        for _ in range(2, n+1):
            ans = a + b
            a, b = b, ans
        return ans