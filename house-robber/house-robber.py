class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        dp = [0]*(len(nums))
        
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]