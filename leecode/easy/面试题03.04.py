class MyQueue:
    def __init__(self):
        self.pushs=[]
        self.pops=[]

    def push(self,x:int):
        self.pushs.append(x)

    def pop(self):
        if len(self.pops)==0:
            while self.pushs:
                self.pops.append(self.pushs.pop())
        return self.pops.pop()

    def peek(self):
        if len(self.pops)==0:
            while self.pushs:
                self.pops.append(self.pushs.pop())
        return self.pops[-1]

    def empty(self):
        if len(self.pops)==0 and len(self.pushs)==0:
            return True
        else:
            return False



    def peek(self):
        pass

    def empty(self):
        pass
