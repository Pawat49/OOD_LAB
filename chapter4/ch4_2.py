class Queue():
    def __init__(self):
        self.queue = []
    def is_empty(self):
        if self.queue:
            return False
        return True
    def sizes(self):
        return len(self.queue)
    def enqueue(self, data):
        self.queue.append(data)
        return self.queue
    def dequeue(self):
        if self.is_empty():
            return "Empty"
        first = self.queue.pop(0)
        return first

print("***Make a group***")
inp = input("Enter input : ").split(",")

max_people = int(inp[0])
person_in_group = inp[1].split()

# สร้างคิวตามที่โจทย์กำหนดมาให้
person_group = Queue()
reject_student = Queue()
group = Queue()
group_no = 0

# นำรายชื่อนักเรียนทั้งหมดเข้าคิว person_group
for person in person_in_group:
    person_group.enqueue(person)

# นำคนออกจากคิวมาจัดกลุ่มทีละคน
while not person_group.is_empty():
    current_person = person_group.dequeue()
    
    # เช็กว่าในกลุ่มมีสีอะไรอยู่บ้างแล้วรวมถึงคนที่กำลังจะเข้ากลุ่มด้วย
    has_green = "Green" in group.queue or current_person == "Green"
    has_pink = "Pink" in group.queue or current_person == "Pink"
    has_blue = "Blue" in group.queue or current_person == "Blue"
    has_yellow = "Yellow" in group.queue or current_person == "Yellow"
    has_red = "Red" in group.queue or current_person == "Red"
    
    conflict = False
    
    # เงื่อนไข 1: Green ห้ามอยู่กลุ่มเดียวกับ Pink เว้นแต่มี Blue
    if has_green and has_pink and not has_blue:
        conflict = True
        
    # เงื่อนไข 2: Blue ห้ามอยู่กลุ่มเดียวกับ Yellow เว้นแต่มี Red
    if has_blue and has_yellow and not has_red:
        conflict = True
        
    # ถ้ามี conflict ให้ส่งคนนั้นเข้าคิว reject_student
    if conflict:
        reject_student.enqueue(current_person)
    else:
        # ถ้าไม่มีปัญหา ให้เข้าคิวกลุ่มปัจจุบัน
        group.enqueue(current_person)
        
        # ถ้าสมาชิกในกลุ่มครบจำนวน max_people ให้แสดงผลแล้วล้างกลุ่มเพื่อเริ่มใหม่
        if group.sizes() == max_people:
            group_no += 1
            print(f"Group {group_no} : {', '.join(group.queue)}")
            group = Queue() # สร้างกลุ่มใหม่

# กรณีที่จัดกลุ่มเสร็จแล้ว แต่กลุ่มล่าสุดยังมีสมาชิกไม่ครบ (เป็นเศษ)
# ให้จับคนในกลุ่มนั้นออกมาเข้าคิว reject ให้หมด
while not group.is_empty():
    reject_student.enqueue(group.dequeue())

# แสดงผลคนที่ถูก Reject
if reject_student.is_empty():
    print("Rejected : None")
else:
    print(f"Rejected : {', '.join(reject_student.queue)}")