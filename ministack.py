class MiniStack():
    def __init__(self,input):
        self.input = input
        self.arr = []
        for i in  self.input :
            if type(i) == int:
                self.arr.append(i)
    def push(self,item):
         self.arr.append(item)
    def remove(self):
         self.arr.pop()
    def top(self):
        print( self.arr[-1])
    def getMin(self):
        print(min(self.arr))
input = MiniStack(["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"])

input.getMin()#; // return 0
input.remove()
input.top()#    // return 2
input.getMin()