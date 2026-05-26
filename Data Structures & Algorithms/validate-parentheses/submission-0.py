class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        val = {'(' : ')' , '{' : '}' , '[' : ']'}
        for char in s:
            if char in val:
                stack.append(char)
            else:
                if stack and val[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return not stack