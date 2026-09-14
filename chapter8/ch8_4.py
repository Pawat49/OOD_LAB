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
        if x is None:
            return x
        bf = x.balance()
        x.setheight()
        if bf == 2:
            if x.left.balance() < 0:
                x.left = self.rotate_right_child(x.left)
            x = self.rotate_left_child(x)

        elif bf == -2:
            if x.right.balance() > 0:
                x.right = self.rotate_left_child(x.right)
            x = self.rotate_right_child(x)

        x.setheight()
        return x
    
    def path(self,node,hp):
        final_path,final_hp,died_node = self._path(node,hp)
        return final_path,final_hp,died_node
    def _path(self,node,hp,died_node=None,path=""):
        if node is None:
            return path[:-3],hp,died_node
        if hp < 0:
            return path[:-3],hp,node.val

        hp -= node.val

        path += str(node.val)
        path,hp,died_node = self._path(node.left,hp,node.val,path+" -> ")
        # path += " ->"
        return path,hp,died_node
        

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

inp = input("Enter Input : ").split("/")
tree = [int(i) for i in inp[0].split()]
hp = int(inp[1])
def DUNGEON(tree,hp):
    avl_tree = AVLTree()
    if tree == []:
        print("EMPTY DUNGEON!")
        return
    for t in tree:
        root = avl_tree.insert(t)
    # printTree90(root)
    
    final_path,final_hp,died_node = avl_tree.path(root,hp)
    if final_hp <= 0:
        print("GAME OVER!")
        print(f"Died Node : {died_node}")
        print(f"HP at death : {final_hp}")
        print(f"Path : {final_path}")
        return
    else:
        print("SUCCESS!")
        print(f"Remaining HP : {final_hp}")
        print(f"Path : {final_path}")
        return
DUNGEON(tree,hp)
# print(tree,hp)