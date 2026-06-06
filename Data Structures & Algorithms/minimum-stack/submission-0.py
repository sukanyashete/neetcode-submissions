class MinStack:

    def __init__(self):
        # this stack to use as a normal stack
        self.stack = []
        # this stack to maintain the minimum at each iteration/element push
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini:
            self.mini.append(val)
        else:
            if self.mini[-1] < val:
                self.mini.append(self.mini[-1])
            else:
                self.mini.append(val)

    def pop(self) -> None:
        if self.stack:
            self.mini.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
