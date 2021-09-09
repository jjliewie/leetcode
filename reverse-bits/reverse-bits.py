class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        k = str(bin(n))[::-1]
        k = k[:-2]
        k = "0b" + k
        
        while len(k) < 34:
            k += "0"
        return int(bin(int(k, 2)), 2)