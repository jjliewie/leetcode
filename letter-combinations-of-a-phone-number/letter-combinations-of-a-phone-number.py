class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        res = [""]
        
        dictionary= {
            '2':"abc", 
            '3':"def", 
            '4':"ghi", 
            '5':"jkl", 
            '6':"mno", 
            '7':"pqrs", 
            '8':"tuv", 
            '9':"wyxz"
        }
        
        for i in digits:
            temp = []
            for j in res:
                for k in dictionary[i]:
                    temp.append(j+k)
            res = temp
            
        return res
        
        