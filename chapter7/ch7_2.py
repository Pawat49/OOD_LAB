class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self,arr):
        self.root = self._insert(self.root,arr,i=0)
    def _insert(self,node,arr,i=0):
        if i >= len(arr) or arr[i] == "null" or arr[i] is None:
            return None
        
        node = Node(int(arr[i]))
        node.left = self._insert(node.left,arr,2*i+1)
        node.right = self._insert(node.right,arr,2*i+2)
        
        
        return node
        # ใช้สูตรหาตำแหน่ง
        # left(i) = 2i + 1
        # right(i) = 2i + 2
        # parrent(i) = (i - 2) // 2
        # root = 0
        # This is valid binary search tree.
        # This isn't valid binary search tree.
        
    def valid(self,node,min_val=float('-inf'),max_val=float('inf')):
        if node is None:
            return True
        
        if min_val >= node.val or node.val >= max_val :
            return False
        
        left_valid = self.valid(node.left,min_val,node.val)
        right_valid = self.valid(node.right,node.val,max_val)
        
        return left_valid and right_valid



def printing(root, dep: int = 0) -> None:
    if(not root): return
    printing(root.right, dep+1)
    print(f"{' '*6*dep}{root.val}")
    printing(root.left, dep+1)

inp = input("Enter data stream : ").split()

bst = BST()

bst.insert(inp)

printing(bst.root)
print()
if bst.valid(bst.root):
    print("This is valid binary search tree.")
else:
    print("This isn't valid binary search tree.")

