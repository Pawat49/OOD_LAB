class AVLNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0
        self.setheight()

    def getheight(self,node):
        if node is None:
            return -1
        else:
            return node.height
        
    def setheight(self):
        self.height = 1 + max(self.getheight(self.left),self.getheight(self.right))
        return self.height
    
    def balance(self):
        return self.getheight(self.left) - self.getheight(self.right)

    def __str__(self):
        return str(self.val)

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self,val):
        self.root,change_left,change_right = self._insert(self.root,val)
        if change_left:
            print("Left Left Rotation")
        elif change_right:
            print("right right Rotation")
        return self.root
    
    def _insert(self,node,val):
        if node is None:
            return AVLNode(val),False,False

        if val < node.val:
            node.left,change_left,change_right = self._insert(node.left,val)
        elif val > node.val:
            node.right,change_left,change_right = self._insert(node.right,val)
        else:
            return node,False,False
        node,change_left,change_right = self.rebalance(node)
        return node,change_left,change_right

    def rotate_left_child(self,x):
        y = x.left
        x.left = y.right
        y.right = x
        x.setheight()
        y.setheight()
        return y
    
    def rotate_right_child(self,x):
        y = x.right
        x.right = y.left
        y.left = x
        x.setheight()
        y.setheight()
        return y
    
    def rebalance(self,node,rotate_left=False,rotate_right=False):
        if node is None:
            return node
        
        bf = node.balance()
        node.setheight()
        change_left = False
        change_right = False

        if bf == 2:
            change_right = True
            if node.left.balance() < 0:
                node.left = self.rotate_right_child(node.left)
            node = self.rotate_left_child(node)
        elif bf == -2:
            change_left = True
            if node.right.balance() > 0:
                node.right = self.rotate_left_child(node.right)
            node = self.rotate_right_child(node)

        node.setheight()
        return node,change_left,change_right

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

print(" *** AVL Tree Insert Element ***")
inp = input("Enter Input : ").split()
tree = [int(i) for i in inp]
avl_tree = AVLTree()
# print(tree)
for i in tree:
    print(f"insert : {i}")
    root = avl_tree.insert(i)
    printTree90(root)
    print("====================")