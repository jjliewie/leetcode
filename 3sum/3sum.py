class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or nums == [0]:
            return []
        result = []
        nums.sort()
        
        for i in range(len(nums)-1):
            j = i+1
            k = len(nums)-1
            while j < k: 
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    if [nums[i], nums[j], nums[k]] not in result:
                        result.append([nums[i], nums[j], nums[k]])
                    k -=1
                    j += 1
                
                if temp > 0:
                    k -= 1
                if temp < 0:
                    j += 1
        return result