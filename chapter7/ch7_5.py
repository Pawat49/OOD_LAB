class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.root = None
        self.leaves = []
    def insert(self,val):
        self.root = self._insert(self.root,val)
        return self.root
    def _insert(self,node,val):
        if node is None:
            return TreeNode(val)

        if val < node.val:
            node.left = self._insert(node.left,val)
        elif val > node.val:
            node.right = self._insert(node.right,val)
        return node
    # root -> left -> right
    def merge_tree(self,node1,node2):
        if node1 is None:
            return None
        if node1.val == node2.val and node1.left is None and node1.right is None:
            return node2
        node1.left = self.merge_tree(node1.left,node2)
        node1.right = self.merge_tree(node1.right,node2)
        return node1
    def get_leaf_values(self,node):
        if node is None:
            return
        if not node.left and not node.right:
            self.leaves.append(node.val)
        self.get_leaf_values(node.left)
        self.get_leaf_values(node.right)
        return self.leaves
    def print_tree(self, node, level=0):
        if node is None:
            return
        self.print_tree(node.right, level + 1)
        print("    " * level + str(node.val))
        self.print_tree(node.left, level + 1)
    def valid(self,node,min_jaa=float('-inf'),max_jaa=float('inf')):
        if node is None:
            return True
        if node.val < min_jaa or node.val > max_jaa:
            return False
        left_valid = self.valid(node.left,min_jaa,node.val)
        right_valid = self.valid(node.right,node.val,max_jaa)
        return left_valid and right_valid

inp = input("Enter trees: ").split("/")
tree1 = [int(i) for i in inp[0].strip().strip("[]").split(",") if i and i != "null"]
tree2 = [int(i) for i in inp[1].strip().strip("[]").split(",") if i and i != "null"]
# print(tree1)
# print(tree2)
print()

bst1 = Solution()
for v1 in tree1:
    bst1.insert(v1)

bst2 = Solution()
for v2 in tree2:
    bst2.insert(v2)
if not tree1 or not tree2:
    print("Cannot merge these trees.")
else:
    leaves_of_tree1 = bst1.get_leaf_values(bst1.root)
    if leaves_of_tree1 and (tree2[0] in leaves_of_tree1):
        bst1.root = bst1.merge_tree(bst1.root,bst2.root)
        if bst1.valid(bst1.root):
            print("Merged successfully:")
            
            bst1.print_tree(bst1.root)
        else:
            print("Cannot merge these trees.")    
    else:
        print("Cannot merge these trees.")