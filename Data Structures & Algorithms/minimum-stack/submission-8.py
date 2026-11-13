class MinStack:

    def __init__(self):
        self.stk = []
        self.min = None

    def push(self, val: int) -> None:
        if len(self.stk) == 0:
            self.stk.append(0)
            self.min = val
        else:
            diff = val - self.min
            self.stk.append(diff)
            if val < self.min:
                self.min  = val
            

    def pop(self) -> None:
        poping   = self.stk.pop()
        if poping > 0:
            return 
        else:
            val  = self.min
            self.min  = self.min - poping

    def top(self) -> int:
        top   = self.stk[-1]  
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
        