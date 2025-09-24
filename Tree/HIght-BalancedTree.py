# Hight-balanced tree means that the height of the two subtrees of any node never differ by more than one.
class TreeNode:
    def __init__(self, value):
        self.value = value
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
    
  
def is_Hight_Balanced(root):
    # base case
    if root is None:
        return True
    # recursive case
    
    is_left = is_Hight_Balanced(root.left)
    is_right = is_Hight_Balanced(root.right)
    is_root = True if abs(fhight(root.left) - fhight(root.right)) <= 1 else False
    
    return is_left and is_right and is_root
    

root = None
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.right = TreeNode(60)
root.left.right.left = TreeNode(70)

print(is_Hight_Balanced(root))
