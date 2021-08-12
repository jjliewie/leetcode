class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range (1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                maximum += prices[i] - prices[i-1]
        return maximum