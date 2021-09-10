class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        l = [str(n) for n in num]
        d = int("".join(l))
        d += k
        result = [int(i) for i in str(d)] 
        return result
        
#         l = ""
        
#         for i in range(len(num)):
#             l += str(num[i])    
#         l = int(l)
#         l += k
#         result = []
#         for t in range(len(str(l))):
#             result.append(int(str(l)[t]))
#         return(result)
# time limit exceeded