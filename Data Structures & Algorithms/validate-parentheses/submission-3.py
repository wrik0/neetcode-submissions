class Solution:
    def isValid(self, s: str) -> bool:
        appendSet = set(['(', '{', '['])
        stack = []
        for char in s:
            if char in appendSet:
                stack.append(char)
            elif char == ')' and len(stack) and stack[-1] =='(':
                stack.pop()
            elif char == '}' and len(stack) and stack[-1] == '{':
                stack.pop()
            elif char == ']' and len(stack) and stack[-1] == '[':
                stack.pop()
            else: return False
        return len(stack) == 0  
