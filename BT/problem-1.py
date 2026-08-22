#17-08-26
#Binary tree=====================
"""

class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

root = Node(10)

root.left = Node(20)
root.right = Node(30)

print(root.data)
print(root.left.data)
print(root.right.data)
"""

#Traversing------------------------
#visiting every noode of the tree
"""
1. Preorder
2. Inorder
3. Post order
4. Lever Order

"""

#preorder

# root->left->right
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node,res):
    if not node:
        return
    res.append(node.data) #root

    preorder(node.left,res)

    preorder(node.right,res)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)

res = []

preorder(root, res)
print(*res)
        
"""
#inorder==========

#left->root->right

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(node,res):
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

"""
#Post order
#left->right-root

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder(node,res):
    if not node:
        return

    postorder(node.left, res)

    postorder(node.right, res)

    res.append(node.data)

    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)

res = []

postorder(root, res)
print(*res)

"""

#level order====
# level wise -l0,l1,l2---

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


from collections import deque

def levorder(root):

    if root is None:
        return

    que = deque([root])

    while que:

        node = que.popleft()

        print(node.data, end=" ")


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

levorder(root)
print(*res)

"""

#DFS using stack=========

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def dfs(root):

    if root is None:
        return

    stack = [root]

    while stack:#1
        node = stack.pop()#3
        print(node.data, end=" ")#1,2,3

        if node.right:#3
            stack.append(node.right)#3

        if node.left:#2
            stack.append(node.left)#3,2
    



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)

res = []

dfs(root)
print(*res) 
"""

#binary search tree
#left side < root < right side--------------
"""
class Node:

    def __init__(self, data):
        self.data =data
        self.left= None
        self.right =None

def insert(root,value):#50,80-70,80-n,80

    if root is None:
        return Node(value)# 80

    if value<root.data:#
        root.left = insert(root.left, value)#n,20

    elif value>root.data:#
        root.right = insert(root.right, value)#n,80

    else:
        print(value, "already existed")

    return root#50



def inorder(root):
    if root is None:
        return

    inorder(root.left)

    print(root.data, end=" ")

    inorder(root.right)

root = None

n = int(input("how many vals do u want to insert"))#7


for i in range(n):#7
    val = int(input("enter val"))#50,30,70,40,60,20,80

    root = insert(root, val)#50,60

print("inorder traversal: ")
inorder(root)


"""