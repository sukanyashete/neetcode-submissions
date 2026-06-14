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
                    num2 = int(stk.pop())
                    num1 = int(stk.pop())
                    if i == "+":
                        stk.append(num1 + num2)
                    elif i == '-':
                        stk.append(num1 - num2)
                    elif i == '*':
                        stk.append(num1 * num2)
                    elif i == '/':
                        #if num1/num2 < 0:
                        #    stk.append(0)
                        #else:
                            stk.append(int(num1/num2))
                    
        return stk[-1]