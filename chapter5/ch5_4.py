
# My algorlithm
# implement class
# D ลบหลังสุดของ linklist
# R เปลี่ยน note เป็นตัวหลัง R
# A เพิ่ม note ตามตัวหลัง A เข้าไปใน linklist
# สร้าง linklist (คร่าวๆ)
# เก็บ node ไปเรื่อยๆจนกว่า node ถัดไปจะเป็น None
# node ประกอบไปด้วย (value,next) value = ค่า next = ค่าตัวถัดไป
# print input ที่เป็น linklist ออกมา
# ทำตาม operation
# เช็คตัวอักษรตัวแรกว่าเป็น A หรือ R หรือ D
# note
# ถ้า D ลบหลังสุดของ linklist
# ถ้า R เปลี่ยน note เป็นตัวหลัง R
# ถ้า A เพิ่ม note ตามตัวหลัง A เข้าไปใน linklist
# print หลัง operation
# เช็คตัวซ้ำ (คร่าวๆ)
# print แบบเอาตัวซ้ำออกแล้ว


# input
# doh re mi fa so la ti / A doh, A re, D, R fa

# output
# ก่อน operation doh -> re -> mi -> fa -> so -> la -> ti
# หลัง operation doh -> re -> mi -> fa -> so -> la -> ti -> fa
# ไม่ซ้ำ note     doh -> re -> mi -> fa -> so -> la -> ti

class Node:

    def __init__(self,value=None,next=None):

        self.value = value

        self.next = next

# 1 -> 2 -> 3 -> None
class LinkList:

    def __init__(self):

        self.head = None
        self.tail = None
        self._size = 0

    

    def appendHead(self,value):

        node = Node(value,self.head)
        
        self.head = node
        self.tail = self.head
        self._size += 1
        return


    def appendLast(self,value):# A
        #CODE HERE
        # if self.head is None and self.tail is None:
        #     print("Error!!!")
        #     return
        current = Node(value)

        if self.head is None:

            self.appendHead(current.value)
            return
        
        self.tail.next = current
        self.tail = current
        self._size += 1
        return
    
    def remove(self,del_node):
        # if self.head is None and self.tail is None:
        #     print("Error!!!")
        #     return
        current = self.head

        if current is del_node:
            self.head = current.next
            return

        while current is not del_node:
            if current.next is del_node:
                remove = current.next
                current.next = remove.next
                self._size -= 1
                return
            current = current.next
            
        return


    

    def removeLast(self): # D
        #CODE HERE
        # if self.head is None and self.tail is None:
        #     print("Error!!!")
        #     return
        if self.head is None:
            print("Error!!!")
            return
        
        if self.head is self.tail:
            self.head = None
            return
        
        current = self.head

        while current.next is not self.tail:
            current = current.next

        remove = self.tail
        current.next = None
        self.tail = current
        self._size -= 1

        return remove


    def rename(self, newName):# R
        #CODE HERE
        if self.head is None:
            print("Error!!!")
            return

        self.tail.value = newName      
        return self.tail.value
            


    def printList(self):
        #CODE HERE
        current = self.head
        
        if self.head is None:
            print("Linklist is empty!")
            return
        
        while current:
            if current.next is not None:
                print(current.value,end = " -> ")
            else:
                print(current.value)
            current = current.next
        
        return

    

    def printListWithNoDuplicate(self):
        #CODE HERE
        if self.head is None:
            print("Linklist is empty!")
            return
        node_previous = self.head
        node_current = self.head.next
        # print(f"node_previous = {node_previous.value} node_current = {node_current.value}")
        while node_previous is not None:
            while node_current is not None:
                # print(f"node_previous = {node_previous.value} node_current = {node_current.value}")
                if node_previous.value == node_current.value:
                    # print(f"remove najaaa")
                    self.remove(node_current)
                    # self.printList()
                    same = True
                node_current = node_current.next
            if node_previous.next is None:
                break
            node_previous = node_previous.next
            node_current = node_previous.next
        
        self.printList()

def convertToLinkList(ls):
    #CODE HERE
    linklist = LinkList()
    for l in ls:
        linklist.appendLast(l)
    return linklist

# def remove_duplicate(list_song):
#     node_previous = list_song.head
#     node_current = node_previous.next
#     while node_previous is not None:
#         while node_current is not None:
#             if node_previous.value == node_current.value:
#                 list_song.remove(node_previous.value)
#             node_current = node_current.next
#         node_previous = node_previous.next
#         node_current = node_previous.next
#     return list_song


    


print("*** My Favourite Keynote ***")

inputl = input("Enter Input / List of operation : ").split('/')

listSong = [ele for ele in inputl[0].strip().split(' ')]

operations = [ele for ele in inputl[1].strip().split(", ")]

# print(f"listSong = {listSong}")
# print(f"operation = {operations}")
# print("-"*70)


myLinkList = convertToLinkList(listSong)
myLinkList.printList()
# #CODE HERE
for i in range(len(operations)):
    op = operations[i].split()
    if op[0] == "A":
        # print(f"{op[0]} {op[1]}")
        myLinkList.appendLast(op[1])
        # myLinkList.printList()
    elif op[0] == "R":
        # print(f"{op[0]} {op[1]}")
        myLinkList.rename(op[1])
        # myLinkList.printList()
    elif op[0] == "D":
        # print(f"{op[0]}")
        myLinkList.removeLast()
        # myLinkList.printList()

myLinkList.printList()
# myLinkList.remove("fa")

myLinkList.printListWithNoDuplicate()

