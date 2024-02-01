class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data > node.data:  # Corrected condition
            node.right = self.insert(node.right, data)
        else:
            node.left = self.insert(node.left, data)
        return node

    def traverse_inorder(self, root):
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data)
            self.traverse_inorder(root.right)

t = Tree()
root = t.createNode(5)
a = [2, 10, 7, 15, 12, 20, 30, 6, 8]
for i in a:
    t.insert(root, i)

t.traverse_inorder(root)
