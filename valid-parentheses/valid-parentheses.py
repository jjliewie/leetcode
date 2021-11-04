class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False
        
        dictionary = {
            '(': ')', '{': '}', '[' : ']'
        }
        
        stack = []
        
        for i in s:
            if i in dictionary:
                stack.append(i)
            else:
                if stack==[]:
                    return False
                
                if i != dictionary[stack.pop()]:
                    return False
                
        return len(stack)==0