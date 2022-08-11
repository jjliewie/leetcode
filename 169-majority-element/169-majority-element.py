class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if cnt == 0:
                cnt += 1
                res = nums[i]
            elif res == nums[i]:
                cnt += 1
            else: cnt -= 1
        return res