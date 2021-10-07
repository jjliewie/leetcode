class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        if not nums or nums == [0]:
                return []
        result = []
        nums.sort()
        
        def threeSum(y, llist, reach):

            for i in range(len(llist)-1):
                j = i+1
                k = len(llist)-1
                while j < k: 
                    temp = llist[i] + llist[j] + llist[k]
                    if temp == reach:
                        if [y, llist[i], llist[j], llist[k]] not in result:
                            result.append([y, llist[i], llist[j], llist[k]])
                        k -=1
                        j += 1

                    if temp > reach:
                        k -= 1
                    if temp < reach:
                        j += 1
        
        for a in range(len(nums)-3):
            threeSum(nums[a], nums[a+1:], target-nums[a])
        return result