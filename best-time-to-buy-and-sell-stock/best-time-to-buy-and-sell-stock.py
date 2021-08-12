class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         maximum = 0
        
#         for i in range(len(prices)-1):
#             for j in range(i+1, len(prices)):
#                 if prices[j]-prices[i] > maximum:
#                     maximum = prices[j]-prices[i]
        
#         return maximum
# brute force :(

        
        minimum = 10000000
        maximum = 0
        
        for i in range(len(prices)):
            if(prices[i] < minimum):
                minimum = prices[i]
            
            if(prices[i] - minimum > maximum):
                maximum = prices[i] - minimum
        
        return maximum