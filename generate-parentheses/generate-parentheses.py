class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        #backtracking
        def dfs(left, right, path):
            
            if len(path) == 2*n:
                return res.append(path)
            
            if left < n:
                dfs(left+1, right, path+"(")
            
            if left > right:
                dfs(left, right+1, path + ")")
        
        dfs(0, 0, "")
        
        return res
        
#         final = []
        
#         def including_yak(q):
            
#             if q == 0:
#                 return []
#             if q == 1:
#                 return ["()"]
#             if q == 2:
#                 return ["()()", "(())"]
        
#             result = []
#             yak = []

#             def divisors(k):
#                 for i in range(1, k):
#                     if k%i == 0:
#                         yak.append(i)

#             divisors(q)

#             def in_out(k, t, use):

#                 if k > t:
#                     return use

#                 if not use:
#                     use.append("()")
#                     return in_out(k+1, t, use)

#                 else:
#                     for i in range(len(use)):
#                         use.append(use[i] + "()")
#                         use.append("()" + use[i])
#                         use[i] = "(" + use[i] + ")"

#                     return in_out(k+1, t, use)

#             in_out(1, n, result)

#             for i in yak:
#                 tlist = []
#                 in_out(1, i, tlist)
#                 for k in range(len(tlist)):
#                     tlist[k] *= int(q/i)
#                 result += tlist
                
                
#             return list(set(result))
    
#         if n > 4:
        
#             for i in range(3, n):
#                 r = []

#                 for k in range(len(including_yak(i))):
#                     for j in range(len(including_yak(n-i))):
#                         print(including_yak(i)[k], including_yak(n-i)[j])
#                         r.append(including_yak(i)[k] + including_yak(n-i)[j])
#                         r.append(including_yak(n-i)[j] + including_yak(i)[k])

#                 final += r
                
#             return set(final)
                
#         else:
#             return including_yak(n)

            
        
        
        
        
        