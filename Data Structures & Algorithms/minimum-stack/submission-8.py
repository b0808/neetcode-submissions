class MinStack:

    def __init__(self):
        self.minstack = []
        self.minv = []


        

    def push(self, val: int) -> None:
              
        self.minstack.append(val)
        self.min = min(val,self.minv[-1] if self.minv else val)   
        self.minv.append(self.min)     
        

    def pop(self) -> None:
        self.minstack.pop(-1)
        self.minv.pop(-1)
        

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.minv[-1]
        
