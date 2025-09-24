# Hight-balanced tree means that the height of the two subtrees of any node never differ by more than one.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def is_Hight_Balanced(root):
    # base case
    if root is None:
        return -1,True
    # recursive Case
    
    leftHight,is_left_balanced = is_Hight_Balanced(root.left)
    rightHight,is_right_balanced = is_Hight_Balanced(root.right)
    is_root_balanced = True if abs(leftHight - rightHight) <= 1 else False
    return 1+max(leftHight,rightHight), is_left_balanced and is_right_balanced and is_root_balanced
    
    

root = None
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.right = TreeNode(60)
root.left.right.left = TreeNode(70)

print(is_Hight_Balanced(root))
