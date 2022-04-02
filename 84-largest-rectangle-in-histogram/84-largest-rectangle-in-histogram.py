class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack, res, use = [], 0, heights+[0]
        
        for x, y in enumerate(use):
            
            while stack and heights[stack[-1]] >= y:
                
                height = heights[stack.pop()]
                
                if not stack: width = x
                else: width = (x-1) - stack[-1]
                
                area = height * width
                res = max(res, area)
                
            stack.append(x)
            
        return res