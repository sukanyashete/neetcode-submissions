class Solution:
    def isValid(self, s: str) -> bool:
        p = {'{':'}', '[':']', '(':')'}
        stack = []

        for i in s:
            if i in p:
                stack.append(i)
            else:
                if (stack and (p[stack.pop()] == i)):
                    continue
                else:
                    return False

        if not stack:
            return True
        else:
            return False
