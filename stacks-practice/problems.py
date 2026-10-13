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



"""
Order	Topic	Priority
1	Stack basics and implementation	High
2	Balanced parentheses	High
3	Next Greater Element	High
4	Queue and circular queue	High
5	Deque and monotonic queue basics	Medium
6	Heap / Priority Queue	Very high
7	BFS and DFS	Very high
8	Dijkstra's Algorithm	Very high
"""

# Balanced parentheses	High

class Stack:
    def __init__(self):
        self.Stack=[]
        









