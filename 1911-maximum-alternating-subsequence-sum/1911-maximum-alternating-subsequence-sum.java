class Solution {
    public long maxAlternatingSum(int[] nums) {
        long ans = 0;
        for(int i = 0; i < nums.length -1; i++){
            ans += Math.max(0, nums[i+1] - nums[i]);
        }
        return ans + nums[0];
    }
}