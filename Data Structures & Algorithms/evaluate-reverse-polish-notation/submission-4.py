class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        num1 = 0
        num2 = 0
        for i in tokens:
            # this lstrip() used because otherwise -ve numbers are not considered as digits and ends up filtering and removing it.
            # that is the negative number won't be appended
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
                        # using int() again on the results because as per question it should round off to 0.
                        # Ref: Assume that division between integers always truncates toward zero.
                        # if I use float division like // then the nearest round off can be -ve numbers too. So strictly using int() so that round-off is always 0.
                        stk.append(int(num1/num2))
                    
        return stk[-1]
