class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        num1 = 0
        num2 = 0
        for i in tokens:
            if i.lstrip('-').isdigit():
                stk.append(int(i))
            else:
                if stk:
                    num2 = stk.pop()
                    num1 = stk.pop()
                    if i == "+":
                        stk.append(num1 + num2)
                    elif i == '-':
                        stk.append(num1 - num2)
                    elif i == '*':
                        stk.append(num1 * num2)
                    elif i == '/':
                        stk.append(int(num1/num2))
                    
        return stk[-1]