class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def buildTree(levelOrder):
    if len(levelOrder) == 0 or levelOrder[0] == -1:
        return None
    
    root = TreeNode(levelOrder[0])
    queue = [root]
    index = 1
    
    while index < len(levelOrder):
        currentNode = queue.pop(0)
        
        # Left Child
        leftValue = levelOrder[index]
        index += 1
        if leftValue != -1:
            leftNode = TreeNode(leftValue)
            currentNode.left = leftNode
            queue.append(leftNode)
        
        if index >= len(levelOrder):
            break
        
        # Right Child
        rightValue = levelOrder[index]
        index += 1
        if rightValue != -1:
            rightNode = TreeNode(rightValue)
            currentNode.right = rightNode
            queue.append(rightNode)
    
    return root
def printTree(root):
    if root is None:
        return
    print(root.data, end=': ')
    if root.left:
        print('L', root.left.data, end=', ')
    if root.right:
        print('R', root.right.data, end='')
    print()
    printTree(root.left)
    printTree(root.right)
TreeInput = [10,20,30,40,50,-1,60,-1,-1,70,-1,-1,-1,-1,-1]
root = buildTree(TreeInput)
printTree(root)