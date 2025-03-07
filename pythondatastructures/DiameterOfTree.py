import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameter(root):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return 0, 0
    ld, lh = diameter(root.left)
    rd, rh = diameter(root.right)
    # diameter is max of lh max(lh+rh+1, ld, rd)
    # 1+max(ld,rd)
    return max(lh+rh+1, ld, rd), 1+max(lh,rh)


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
dia, height = diameter(root)
print(dia)
