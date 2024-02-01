class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data <root.data:
             root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root



def inorder(root):
    if root:
        
        inorder(root.left)
        
       
        print(root.data, end=" ")
        
        
        inorder(root.right)

root =None

while True:
    data=input("Enter Element or quit for :'q'  :  ")
    if data=='q':
        break
    root=insert(root,int(data))

               

print("Sorted order of elements:")
inorder(root)
