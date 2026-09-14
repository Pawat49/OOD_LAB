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
        self.root = self._insert(self.root,val)
        return self.root
    
    def _insert(self,node,val):
        if node is None:
            return AVLNode(val)
        if val < node.val:
            node.left = self._insert(node.left,val)
        elif val > node.val:
            node.right = self._insert(node.right,val)
        else:
            return node
        
        return self.rebalance(node)
    
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

    def rebalance(self,x):
        return
    
    def path(self,hp,path):
        return

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

inp = input("Enter Input : ").split("/")
tree = [int(i) for i in inp[0].split()]
hp = int(inp[1])
avl_tree = AVLTree()
if tree == []:
    print("EMPTY DUNGEON!")
for t in tree:
    root = avl_tree.insert(t)
printTree90(root)
if hp <= 0:
    print("GAME OVER!")
else:
    print("SUCCESS!")
    print(f"Remaining HP : {hp}")
    print(f"Path : ")
print(tree,hp)