class Solution:
    def reverseVowels(self, s: str) -> str:
        
        word = [x for x in s]
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        v = []
        for i in word:
            if i.lower() in vowels:
                v.append(i)
        cnt = 0
        # print(v)
        v.reverse()
        for i in range(len(word)):
            if word[i].lower() in vowels:
                word[i] = v[cnt]
                cnt += 1
                
        return "".join(word)