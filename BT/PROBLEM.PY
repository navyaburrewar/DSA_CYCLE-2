 # class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None

# root=Node(10)
# root.left=Node(20)       
# root.right=Node(30)

# print(root.data)
# print(root.left.data)
# print(root.right.data)





class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preorder(node,res):
    if not node:
        return
    res.append(node.data)

    preorder(node.left,res)
    preorder(node.right,res)    


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(6)


res=[]

preorder(root,res)
print(*res)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(node, res):
    if not node:
        return

    inorder(node.left, res)

    res.append(node.data)

    inorder(node.right, res)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)


res = []

inorder(root, res)
print(*res)




def postorder(node,res):
    if not node:
        return 

    postorder(node.left,res)
    postorder(node.right,res)

    res.append(node.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)

res=[]

postorder(root,res)
print(*res)


### level order

class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

from collections import deque

def levelorder(root):
    if root is None:
        return 
    que=deque([root])

    while que:
        node=que.popleft()
        print(node.data,end=" ")

        if node.left:
            que.append(node.left)

        if node.right:
            que.append(node.right)    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)

res = []

levelorder(root)
print(*res)




###  code for the  dfs

class node:
     def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def  dfs(root):
    if root is None:
        return 
    stack=[root]

    while stack:
        node=stack.pop()

        print(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

root=node(1)

root.left=node(2)
root.right=node(4)

root.left.left=node(4)
root.left.right=node(8)

print("dfs preorder traversal:")

dfs(root)




#  inserting at a particular position


class node:
     def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def  dfs(root):
    if root is None:
        return 
    stack=[root]

    while stack:
        node=stack.pop()

        print(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)




root=node(1)

root.left=node(2)
root.right=node(4)

root.left.left=node(4)
root.left.right=node(8)




print("dfs preorder traversal:")

dfs(root)



