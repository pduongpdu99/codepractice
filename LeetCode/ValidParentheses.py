class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        end = []
        for i in range(0, len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(i)
            
            if s[i] in [')', '}', ']']:
                end.append(s[i])
                if len(stack) == 0:
                    return False

                if s[i] == ')' and s[stack[-1]] == '(':
                    stack.pop()
                    end.pop()
                elif s[i] == '}' and s[stack[-1]] == '{':
                    stack.pop()
                    end.pop()
                elif s[i] == ']' and s[stack[-1]] == '[':
                    stack.pop()
                    end.pop()

                
        return len(stack) == len(end) == 0
