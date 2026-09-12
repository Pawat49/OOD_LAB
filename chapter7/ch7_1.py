class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
        self.root = self._insert(self.root,data)
        return self.root
    def _insert(self,node,data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self._insert(node.left,data)
        elif data > node.data:
            node.right = self._insert(node.right,data)
        return node

    def findDepth(self, node, key, depth = 0):
        # Code Here
        # not found return -1
        if node == None:
            return -1
        if key == node.data:
            return depth
        
        if key < node.data:
            return self.findDepth(node.left,key,depth+1)
        elif key > node.data:
            return self.findDepth(node.right,key,depth+1)
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
values = inp[:-1]
key = inp[-1]

for i in values:
    root = T.insert(i)
T.printTree(root)
print('-' * 50)
print(f"Depth of {key} : {T.findDepth(root, key)}")
