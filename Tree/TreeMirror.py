class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def mirror(root):
    if root is None:
        print(-1,end=" ")
        return
    print(root.val,end=" ")
    root.left,root.right = root.right,root.left
    mirror(root.left)
    mirror(root.right)
    
def prinnt(root):
    if root is None:
        print(-1,end=" ")
        return 
    
    print(root.val,end=" ")
    prinnt(root.left)
    prinnt(root.right)
    
root = None # Tree is empty
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.left.right.left = TreeNode(70)
root.right.right = TreeNode(60)

prinnt(root)

print("\n Mirror:--> ")
mirror(root)