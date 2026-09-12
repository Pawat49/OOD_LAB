class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,val):
        self.root = self._insert(self.root,val)
    def _insert(self,node,val):
        if node is None:
            return Node(val)
        
        if val < node.val:
            node.left = self._insert(node.left,val)
        
        if val > node.val:
            node.right = self._insert(node.right,val)
        
        return node
    def delete(self,node,low,high):
        if node is None:
            return node
        # if low <= node.val <= high:
        #     return node
        if node.val < low:
            return self.delete(node.right,low,high)
        if node.val > high:
            return self.delete(node.left,low,high)
        node.left = self.delete(node.left,low,high)
        node.right = self.delete(node.right,low,high)
        return node
    def sum(self,node,sum=0):
        if node is None:
            return sum

        sum = self.sum(node.left,sum+node.val)
        sum = self.sum(node.right,sum)

        return sum
def printing(root, dep: int = 0) -> None:
    if not root:
        return
    printing(root.right, dep + 1)
    print(f"{' ' * (1 + 5 * dep)}{root.val}")
    printing(root.left, dep + 1)

print("***Range Sum***")
inp = input("Enter input : ").split("/")
bst = BST()
print()
print("Binary Search Tree:")

for i in inp[0].split():
    bst.insert(int(i))

printing(bst.root)
low = int(inp[1].strip())
high = int(inp[2].strip())
print()
print(f"Range : [{low}, {high}]")
bst.root = bst.delete(bst.root,low,high)
printing(bst.root)
print(f"Sum of nodes in range = {bst.sum(bst.root)}")

