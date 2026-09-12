class Node():
    def __init__(self,val,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkList():
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return self.head

        current = self.head
        while current.next is not None:
            current = current.next

        new_node.prev = current
        new_node.next = None
        self.tail.next = new_node
        self.tail = self.tail.next
        return self.tail
    def reverse(self):
        if self.head is self.tail:
            print(f"{self.head.val} -> {self.head.next}")
            return
        self.head = self.tail
        current = self.head
        while current is not None:
            if current.prev is None:
                print(f"{current.val} -> {current.prev}")
                return
            print(f"{current.val} -> ",end="")
            current = current.prev
    def show(self):
        if self.head is self.tail:
            print(f"{self.head.val} -> {self.head.next}")
            return
        current = self.head
        while current is not None:
            if current.next is None:
                print(f"{current.val} -> {current.next}")
                return
            print(f"{current.val} -> ",end="")
            current = current.next
            
        

inp = input("Enter input : ").split("->")
print(inp)
l = LinkList()
for i in inp:
    l.append(i)
l.show()
l.reverse()



