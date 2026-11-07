class MinStack:

    def __init__(self):
        self.stk  = []
        self.min_till_now = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.min_till_now) == 0:
            self.min_till_now.append(val)
        else:
            if self.min_till_now[-1] > val:
                self.min_till_now.append(val)
            else:
                self.min_till_now.append(self.min_till_now[-1])


    def pop(self) -> None:
        if len(self.stk) > 0 :
            poping = self.stk.pop(-1)
            self.min_till_now.pop(-1)
            return poping
        else:
            raise Exception("stack is empty")

    def top(self) -> int:
        if len(self.stk) > 0:
            return self.stk[-1]
        else:
            raise Exception("stack is empty")
        

    def getMin(self) -> int:
        if len(self.min_till_now) != 0:
            return self.min_till_now[-1]
        else:
            raise Exception("stack is empty")
        
