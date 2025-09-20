class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
        
def fsum(root,s):
    if root is None:
        return
    
    
    s[0] = s[0] + root.val
    
    fsum(root.left,s)
    fsum(root.right,s)
    return s
    
    
root = None # Tree is empty
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.left.right.left = TreeNode(70)
root.right.right = TreeNode(60)

s = [0]
print(fsum(root,s))