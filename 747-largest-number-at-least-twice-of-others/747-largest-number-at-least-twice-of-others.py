class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        k = nums.index(max(nums))
        if 2 * max(nums[:k] + nums[k+1:]) <= nums[k]:
            return k
        return -1