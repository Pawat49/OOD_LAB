class TreeNode(object): 
    def __init__(self, val): 
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
        # left - right
        return self.getheight(self.left) - self.getheight(self.right)

    def __str__(self):
        return str(self.val)

class AVL_Tree(object): 
    #code here
    def __init__(self):
        self.root = None
    def insert(self,val):
        self.root,change = self._insert(self.root,val)
        if change :
            print("Not Balance, Rebalance!")
        return self.root
    def _insert(self,node,val):
        if node is None:
            return TreeNode(val),False

        if val < node.val:
            node.left,change = self._insert(node.left,val)
        elif val > node.val:
            node.right,change = self._insert(node.right,val)
        else:
            return node,False
        node, is_rotated = self.rebalance(node)
        change = change or is_rotated
        return node,change
    def rotate_left_leaf(self,x):
        y = x.left
        x.left = y.right
        y.right = x
        x.setheight()
        y.setheight()
        return y
    def rotate_right_leaf(self,x):
        y = x.right
        x.right = y.left
        y.left = x
        x.setheight()
        y.setheight()
        return y
    def rebalance(self,x,balance=False):
        if x is None:
            return x,False
        
        x.setheight()
        bf = x.balance()
        change = False

        if bf == 2:
            if x.left.balance() < 0:
                x.left = self.rotate_right_leaf(x.left)
            x = self.rotate_left_leaf(x)
            change = True

        elif bf == -2:
            if x.right.balance() > 0:
                x.right = self.rotate_left_leaf(x.right)
            x = self.rotate_right_leaf(x)
            change = True
        
        x.setheight()
        return x,change
    
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(int(e))
    printTree90(root)
    print("===============")