class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        
        start = 0
        end = len(height)-1
        
        while start != end:
            max_area = max(max_area, min(height[start], height[end]) * (end-start))
            
            if height[start] > height[end]:
                end -=1
            else:
                start += 1
        
        print(max_area)
        
        return(max_area)