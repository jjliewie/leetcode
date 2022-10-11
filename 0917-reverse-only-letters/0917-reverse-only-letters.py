class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = [c for c in s if c.isalpha()]
        return "".join(stack.pop() if c.isalpha() else c for c in s)