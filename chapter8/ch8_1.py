class AVLNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0
        self.setheight()

    def __str__(self):
        return str(self.val)
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
        else:
            node.right = self._insert(node.right,val)
        return self.rebalance(node)
    def print_tree(self, node, level=0):
        if node is None:
            return
        self.print_tree(node.right, level + 1)
        print("    " * level + str(node.val))
        self.print_tree(node.left, level + 1)
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
        x.setheight()
        bf = x.balance()
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
    def search(self, root, small):
        result, _ = self._search(root, small, 1)
        return result

    def _search(self, node, small, k):
        if node is None:
            return None, k

        left_found, k = self._search(node.left, small, k)
        if left_found is not None:
            return left_found, k

        if k == small:
            return node, k

        return self._search(node.right, small, k + 1)
print("*** Simple but more ***")
inp = input("input  N node, Data, K small : ").split(",")
n_node = int(inp[0])
data_in_tree = [int(i) for i in inp[1].split()]
smallest = int(inp[2])
# print(n_node,data_in_tree,smallest)
avl_tree = AVLTree()
for i in data_in_tree:
    root = avl_tree.insert(i)
# avl_tree.print_tree(root)
print(avl_tree.search(root,smallest))
