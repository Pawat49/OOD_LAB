# A2. Undo/Redo Editor (ระดับ: กลาง, 20 คะแนน)

# ออกแบบคลาส TextEditor ที่มี:

# type(ch) — เพิ่มตัวอักษรท้ายข้อความ
# delete() — ลบตัวท้าย
# undo() — ย้อนคำสั่งล่าสุด
# redo() — ทำคำสั่งที่ undo ไปแล้วซ้ำ
# text() — คืนข้อความปัจจุบัน
# python
# e = TextEditor()
# e.type('a'); e.type('b'); e.delete()
# e.text()   # "a"
# e.undo()   # ย้อน delete
# e.text()   # "ab"
# e.redo()
# e.text()   # "a"
# e.type('z')
# e.redo()   # ต้องไม่มีผล -- redo ถูกล้างไปแล้ว
# e.text()   # "az"


# A2 — TextEditor

# เขียนเป็น sequence เพราะเป็น stateful object

# doubly linklist
# a <-> b <-> c
class DoublyNode():
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class TextEditor():
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    def type(self,val):
        new_node = DoublyNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self._size += 1
            return self.head
        
        current = self.head

        while current.next is not None:
            current = current.next

        new_node.prev = current
        new_node.next = None
        self.tail.next = new_node
        self.tail = self.tail.next
        self._size += 1
        return self.tail
    def text(self):
        text = ""
        if self.head is self.tail:
            text += self.head.val
            # print(text,end="")
            return text
        
        current = self.head
        while current is not self.tail:
            text += current.val
            # print(text,end="")
            current = current.next
        text += self.tail.val
        # print(text,end="")
        return text
    def undo(self):
        current = self.tail
        
        if self.tail.next is not None:
            self.tail = self.tail.prev
            return self.tail

        self.tail = current
        return self.tail
    def redo(self):
        self.tail = self.tail.next
        return self.tail
    def delete(self):
        current = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return current

# T1 — ปกติ

e = TextEditor()
e.type('a'); e.type('b'); e.type('c')
assert e.text() == "abc"
e.undo(); assert e.text() == "ab"
e.undo(); assert e.text() == "a"
e.redo(); assert e.text() == "ab"

# T2 — undo ข้าม delete

e.type('a'); e.type('b'); e.delete()
assert e.text() == "a"
e.undo(); assert e.text() == "ab"   # delete ต้องคืนตัวอักษรเดิมกลับมา

# เคสนี้วัดว่า "ตอน delete นายจำไว้ไหมว่าลบตัวอะไรไป" ถ้าจำแค่ว่า "ทำ delete" จะ undo ไม่ได้

# T3 — redo ถูกล้าง (ข้อสอบชอบมาก)

# e.type('a'); e.type('b')
# e.undo()                 # text = "a"
# e.type('z')              # action ใหม่
# e.redo()                 # ต้องไม่มีผล
# assert e.text() == "az"

# # T4 — edge: undo/redo เกินขอบ

# e = TextEditor()
# e.undo(); e.undo()        # ต้องไม่ crash
# assert e.text() == ""
# e.redo()                  # ต้องไม่ crash
# assert e.text() == ""
# e.delete()                # ลบตอนว่าง ต้องไม่ crash
# assert e.text() == ""

# # T5 — edge: undo ทั้งหมดแล้ว redo ทั้งหมด

# for ch in "hello": 
#     e.type(ch)
# for _ in range(5): 
#     e.undo()
# assert e.text() == ""
# for _ in range(5): 
#     e.redo()
# assert e.text() == "hello"

