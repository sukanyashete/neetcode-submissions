class Solution:
    def isValid(self, s: str) -> bool:
        p = {'}':'{', ']':'[', ')':'('}
        stack = []

        #Odd lengths cannot be balanced hence return false
        if (len(s)%2) != 0:
            return False

        for i in s:
            if i in p:
                # If stack is empty OR the top doesn't match, it's invalid
                if not stack or (p[i] != stack.pop()):
                    return False
            else:
                # It's an opening bracket, push it
                stack.append(i)

        return not stack
