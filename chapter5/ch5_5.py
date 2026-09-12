class DoublyNode:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def visit(self, page):
        new_node = DoublyNode(page)
        
        # กรณีที่ไม่มีประวัติเลย
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            # เงื่อนไขที่ 3: เมื่อใช้ VISIT หลังจากกด BACK 
            # ประวัติที่อยู่ด้านหน้าทั้งหมด (ต่อจาก current) ต้องถูกลบออก
            self.current.next = new_node
            new_node.prev = self.current
            self.tail = new_node
            self.current = new_node

    def back(self, k):
        # ย้อนกลับไม่เกิน k หน้า (เงื่อนไขที่ 4: หยุดที่หน้าแรกหากเกิน)
        while k > 0 and self.current and self.current.prev:
            self.current = self.current.prev
            k -= 1

    def forward(self, k):
        # เดินหน้าไม่เกิน k หน้า (เงื่อนไขที่ 5: หยุดที่หน้าสุดท้ายหากเกิน)
        while k > 0 and self.current and self.current.next:
            self.current = self.current.next
            k -= 1

    def print_current(self):
        # เงื่อนไขที่ 6: หากไม่มีประวัติ ให้แสดง Empty
        if self.current is None:
            print("Empty")
        else:
            print(self.current.value)

    def print_history(self):
        # เงื่อนไขที่ 6: หากไม่มีประวัติ ให้แสดง Empty
        if self.head is None:
            print("Empty")
            return

        nodes = []
        curr = self.head
        while curr:
            if curr == self.current:
                nodes.append(f"[{curr.value}]")
            else:
                nodes.append(curr.value)
            curr = curr.next
        
        print(" <-> ".join(nodes))

    def remove(self, page):
        curr = self.head
        target = None

        # ค้นหาโหนดแรกที่ตรงกับ page
        while curr:
            if curr.value == page:
                target = curr
                break
            curr = curr.next

        # เงื่อนไขที่ 7: หากไม่พบเว็บไซต์ ให้แสดง Not found: page
        if target is None:
            print(f"Not found: {page}")
            return

        # เงื่อนไขที่ 8: หากลบหน้าปัจจุบัน ให้เลือกหน้าถัดไปเป็นหน้าปัจจุบันใหม่ 
        # หากไม่มีหน้าถัดไปจึงเลือกหน้าก่อนหน้า
        if target == self.current:
            if target.next:
                self.current = target.next
            else:
                self.current = target.prev

        # ตัดการเชื่อมโยงของ target ออกจาก Linked List
        if target.prev:
            target.prev.next = target.next
        else:
            self.head = target.next  # หากเป็น head โหนดแรก

        if target.next:
            target.next.prev = target.prev
        else:
            self.tail = target.prev  # หากเป็น tail โหนดสุดท้าย

    def clear(self):
        self.head = None
        self.tail = None
        self.current = None


def main():
    # รับคำสั่งทั้งหมดครั้งเดียว
    raw_input = input(">>").strip()
    if not raw_input:
        return

    tokens = raw_input.split()
    browser = DoublyLinkList()
    i = 0

    while i < len(tokens):
        cmd = tokens[i]

        if cmd == "VISIT":
            page = tokens[i+1]
            browser.visit(page)
            i += 2
        elif cmd == "BACK":
            k = int(tokens[i+1])
            browser.back(k)
            i += 2
        elif cmd == "FORWARD":
            k = int(tokens[i+1])
            browser.forward(k)
            i += 2
        elif cmd == "CURRENT":
            browser.print_current()
            i += 1
        elif cmd == "HISTORY":
            browser.print_history()
            i += 1
        elif cmd == "REMOVE":
            page = tokens[i+1]
            browser.remove(page)
            i += 2
        elif cmd == "CLEAR":
            browser.clear()
            i += 1
        elif cmd == "END":
            break
        else:
            i += 1

if __name__ == "__main__":
    main()