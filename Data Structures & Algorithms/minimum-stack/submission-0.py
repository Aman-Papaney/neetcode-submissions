class MinStack:

    def __init__(self):
        self.stack = []
        self.top_ind = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.top_ind += 1

    def pop(self) -> None:
        self.stack.pop(self.top_ind)
        self.top_ind -= 1

    def top(self) -> int:
        return self.stack[self.top_ind]

    def getMin(self) -> int:
        return min(self.stack)
        
