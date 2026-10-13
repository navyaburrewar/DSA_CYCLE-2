class Stack:
    def __init__(self):
        self.Stack=[]

    def push(self,x):
        self.Stack.append(x)
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.Stack.pop()
    def size(self):
        return len(self.Stack)
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.Stack[-1]
    def is_empty(self):
        return len(self.Stack)==0
        
s=Stack()
s.push(20)
s.push(40)
s.push(50)

print(s.peek())
print(s.pop())
print(s.size())
print(s.is_empty())




