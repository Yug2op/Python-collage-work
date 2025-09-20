# s[0] = 0
# s = 0 which takes more space??


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
        
def fhight(root):
    # base case
    if root is None:
        return -1
    # recursive Case
    
    leftHight = fhight(root.left)
    rightHight = fhight(root.right)
    
    return 1+max(leftHight,rightHight)
    
    
root = None # Tree is empty
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.left.right.left = TreeNode(70)
root.right.right = TreeNode(60)


print(fhight(root))
