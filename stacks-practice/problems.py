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
s.push(28)
s.push(40)
s.push(39)
s.push(90)
s.push(100)
s.push(50)
s.push(90)

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

# Balanced parentheses	High problem...

# class Stack:
#     def __init__(self):
#         self.Stack=[]
#     parenthesis={
#         "(":")",
#         "{":"}",
#         "[":"]"
#     }    
#     def push(self,x):
#         self.satck.append(x)
#     def pop(self):
#         return self.stack.pop()
#     def is_empty(self):
#         return len(self.stack) == 0
    









