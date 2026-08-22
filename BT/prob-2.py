class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=node(3)
root.left=node(4)
root.right=node(10)
root.left.left=node(18)
root.right.right=node(67)  

print(root.left.left.data)
print(root.right.right.data)
print(root.left.data)

## travelsing 

#3 pre-order
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preorder(node,res):
    if node is None:
        return
    res.append(node.data)
    preorder(node.left,res)
    preorder(node.right,res)


root=node(10)
root.left=node(4)
root.right=node(11)
root.left.left=node(18)
root.right.right=node(67)  


res=[]
preorder(root,res)
print(*res)




### inorder

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(node,res):
    if not node:
        return 
    inorder(node.left,res)
    res.append(node.data)
    inorder(node.right,res)


root=node(10)
root.left=node(4)
root.right=node(11)
root.left.left=node(18)
root.right.right=node(67) 


res=[]
inorder(root,res)
print(*res)



class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def postorder(node,res):
    if not node:
        return
    postorder(node.left,res)
    postorder(node.right,res)
    res.append(node.data)        

root=node(10)
root.left=node(4)
root.right=node(11)
root.left.left=node(18)
root.right.right=node(67) 

res=[]

postorder(root,res)
print(*res)

  
#  level order
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
from collections import deque
def levelorder(root):
    if not root :
        return 
    que=deque([root])

    while que:
        node=que.popleft()
        print(node.data,end=" ")

        if node.left:
            que.append(node.left)
        if node.right:    
            que.append(node.right)

root=node(10)
root.left=node(4)
root.right=node(11)
root.left.left=node(18)
root.right.right=node(67) 


levelorder(root)
















 
       
            




