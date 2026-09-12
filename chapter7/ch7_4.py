class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)
class BST:
    def __init__(self):
        self.root = None
    def insert(self,val):
        self.root = self._insert(self.root,val)
        return self.root
    def _insert(self,node,val):
        if node is None:
            return Node(val)
        
        if val < node.val:
            node.left = self._insert(node.left,val)
        elif val > node.val:
            node.right = self._insert(node.right,val)
        return node
    def printTree(self, node, level = 0):
            if node != None:
                self.printTree(node.right, level + 1)
                print('     ' * level, node)
                self.printTree(node.left, level + 1)
    def traversal(self, node, treasure, escape, s="❌ ", found_treasure=False, found_escape=False):
        # 1. ปลายทางหรือทางตัน
        if node is None:
            return False

        current_found_treasure = found_treasure
        current_found_escape = found_escape

        # ตรวจสอบสมบัติ
        if node.val == treasure:
            print("Found Treasure !!!")
            current_found_treasure = True

        # ตรวจสอบทางออก: ต้องเจอสมบัติมาก่อน (หรือเจอที่โหนดนี้พร้อมกัน) เท่านั้น
        if node.val == escape and current_found_treasure:
            print("Found Escape !!!")
            current_found_escape = True

        # จัดการข้อความแสดงผล
        if current_found_treasure and current_found_escape:
            s = "✅" + s[1:] + str(node.val)
        else:
            s += str(node.val)

        print(s)

        # 2. เมื่อเจอสมบัติแล้วและเจอทางออกต่อตามลำดับ ให้หยุดทันที
        if current_found_treasure and current_found_escape:
            return True

        s += " -> "

        # 3. เดินทางต่อซ้าย-ขวา แบบ Short-circuit
        if self.traversal(node.left, treasure, escape, s, current_found_treasure, current_found_escape):
            return True

        if self.traversal(node.right, treasure, escape, s, current_found_treasure, current_found_escape):
            return True

        return False

bst = BST()
inp = input("Enter Input : ").split("/")
space = [int(i) for i in inp[0].split()]
treasure = int(inp[1])
escape = int(inp[2])
# print(space)
for i in space:
    root = bst.insert(i)
bst.printTree(root)
print("-------------------------------------------------")
if bst.traversal(root,treasure,escape):
    print(">>> Mission Complete <<<")
else:
    print(">>> Mission Failed <<<")

