class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
root=Node(1)
root.left=Node(10)
root.right=Node(20)
inorder(root)