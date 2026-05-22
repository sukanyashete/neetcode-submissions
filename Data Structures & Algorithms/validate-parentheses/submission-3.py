class Solution:
    def isValid(self, s: str) -> bool:
        p = {'{':'}', '[':']', '(':')'}
        stack = []
        for i in s:
            if i not in p:
                if stack:
                    b = stack.pop()
                    if p[b] != i:
                        return False
                else:
                    return False
            else:
                stack.append(i)
        
        if not stack:
            return True
        else:
            return False
