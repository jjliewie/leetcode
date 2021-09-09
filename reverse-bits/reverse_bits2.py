class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        # print(1<<2)
        for i in range(32):
            res = res<<1 ^(n&1)
            n >>= 1
        return res
    
# using bit operations
