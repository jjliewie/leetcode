class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        a = sorted(intervals, key=lambda x:(x[0], x[1]))
        result = [a[0]]
        
        for i in range(1, len(a)):
            if a[i][0] <= result[-1][1]:
                if a[i][1] >= result[-1][1]:
                    result[-1] = [result[-1][0], a[i][1]]
            else:
                result.append(a[i])
                
        return(result)
        
        