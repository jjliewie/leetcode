class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        idx = defaultdict(list)
        for i,t in enumerate(nums):
            idx[t].append(i)
        degree = max(list(map(len, idx.values())))
        k = float('inf')
        for v in idx.values():
            if len(v)==degree:
                k = min(k, (v[-1]-v[0]))
        return k + 1
        
        
#         recursive way;;; but time limit exceeded
        
#         def degree(t):
#             d = 0
#             for k in set(t):
#                 d = max(d, t.count(k))
#             return d
        
#         if degree(nums) == degree(nums[1:len(nums)-1]):
#             return self.findShortestSubArray(nums[1:len(nums)-1])
#         elif degree(nums) == degree(nums[1:]):
#             return self.findShortestSubArray(nums[1:])
#         elif degree(nums) == degree(nums[:len(nums)-1]):
#             return self.findShortestSubArray(nums[:len(nums)-1])
#         else:
#             return len(nums)
