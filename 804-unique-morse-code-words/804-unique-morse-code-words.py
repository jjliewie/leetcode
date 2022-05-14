class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_conv = []
        for word in words:
            res=""
            for char in word:
                res += morse[ord(char)-97]
            morse_conv.append(res)
        return len(set(morse_conv))
        