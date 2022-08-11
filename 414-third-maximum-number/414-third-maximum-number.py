class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        cur = 1
        first = max(nums)
        while nums:
            m = max(nums)
            if cur == 3: return m
            c = nums.count(m)
            for i in range(c):
                nums.remove(m)
            cur += 1
        return first