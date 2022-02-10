class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        return sum([max(0, nums[i+1] - nums[i]) for i in range(len(nums)-1)]) + nums[0]
        
#         ans = 0
#         for i in range(len(nums)-1):
#             ans += max(0, nums[i+1] - nums[i])

#         return ans + nums[0]