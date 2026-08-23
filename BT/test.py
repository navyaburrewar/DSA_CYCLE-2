"""
## binary tree traversals

class Node:
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

def inorder(node,res):
    if node is None:
        return 
    inorder(node.left,res)
    res.append(node.data)
    inorder(node.right,res)


def postorder(node,res):
    if node is None:
        return 
    postorder(node.left,res)
    postorder(node.right,res)
    res.append(node.data)
       


root=int(input("root value: "))
a=int(input("root of left: "))
b=int(input("root of right: "))
c=int(input("root of left.right: "))
d=int(input("root of left.left: "))
e=int(input("root of right.right: "))
f=int(input("root of right.left: "))

root=Node(root)
root.left=Node(a)
root.right=Node(b)

root.left.left=Node(c)
root.left.right=Node(d)

root.right.left=Node(e)
root.right.right=Node(f)

    
    
res=[]
preorder(root,res)
print("preorder",*res)


res=[]
inorder(root,res)
print("inorder",*res)


res=[]
postorder(root,res)
print("postorder",*res)



### 2 level order traversal

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
from collections import deque
def levelorder(node):
    if not node:
        return 
    que=deque([root])
    while que:
        node=que.popleft()
        print(node.data,end=" ")

        if node.left:
            que.append(node.left)

        if node.right:
            que.append(node.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)


levelorder(Node)    

"""
# binary serach tree insertion

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def bst(node,value):
#     if node is None:
#         return 
#     if value<node.
            



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def bst(node,value):
#     if node is None:
#         return 
#     if value<node.
            

                




