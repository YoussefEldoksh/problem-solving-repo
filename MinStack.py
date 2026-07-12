from collections import deque

class MinStack:

    def __init__(self):
        self.items = deque()
        self.mins = deque()

    def push(self, value: int) -> None:
        self.items.append(value)
        if self.mins:
            self.mins.append(min(value,self.mins[-1]))
        else:
            self.mins.append(value)
            
    def pop(self) -> None:
        if not len(self.items) == 0:
            self.mins.pop()
            return self.items.pop()
        else: return None

    def top(self) -> int:
        if not len(self.items) == 0:
            return self.items[-1]
        else: return None

    def getMin(self) -> int:
        if not len(self.items) == 0:
            return self.mins[-1]
        else: return None




# Your MinStack object will be instantiated and called as such:
value = 1
obj = MinStack()
obj.push(value)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()