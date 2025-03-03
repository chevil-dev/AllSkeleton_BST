class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = None

def allSkeleton(start, end):
    if start > end :
        return [None]

    allTrees = []
    for i in range(start, end + 1):
        leftTrees = allSkeleton(start, i - 1)
        rightTrees = allSkeleton(i + 1, end)

        for left in leftTrees:
            for right in rightTrees:
                currentNode = Node(i)
                currentNode.left = left
                currentNode.right = right
                allTrees.append(currentNode)

    return allTrees
