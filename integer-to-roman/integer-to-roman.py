class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        answer = ''
        
        roman = {
            1000 : 'M', 
            500 : 'D', 
            100 : 'C',
            50 : 'L',
            10 : 'X', 
            5 : 'V',
            1 : 'I', 
        }

        for index, digit in enumerate(str(num)[::-1]):
            if int(digit) != 0:
                result.append(int(digit + ('0' * index)))
        result = result[::-1]
        
        print(result)
        
        for i in range(len(result)):
            while result[i] >0:
                if str(result[i])[0] != '9' and  str(result[i])[0] != '4':
                    for k in roman:
                        while result[i]-k >=0:
                            result[i]-=k
                            answer += roman[k]
                else:
                    for k in roman:
                        if result[i]-k >=0 and str(k)[0] == '1':
                            result[i]+=k
                            answer += roman[k]
                            break
            
        print(answer)
        
        return answer
    
    # long solution