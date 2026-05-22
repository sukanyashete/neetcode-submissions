class Solution:
    def isValid(self, s: str) -> bool:
        #p = {'{':'}', '[':']', '(':')'}
        p = {'}':'{', ']':'[', ')':'('}
        stack = []

        #Odd lengths cannot be balanced hence return false
        if (len(s)%2) != 0:
            return False

        for i in s:
            if i in p:
                if stack and (p[i] == stack.pop()):
                    continue
                else:
                    return False
            else:
                stack.append(i)

        return not stack
