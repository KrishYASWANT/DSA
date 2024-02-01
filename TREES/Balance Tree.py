class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_balanced(root):
    if root is None:
        return True

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    if abs(left_height - right_height) <= 1 and
    is_balanced(root.left) and is_balanced(root.right):
        return True

    return False

def get_height(node):
    if node is None:
        return 0

    return max(get_height(node.left), get_height(node.right)) + 1


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

if is_balanced(root):
    print("The binary tree is balanced.")
else:
    print("The binary tree is not balanced.")
