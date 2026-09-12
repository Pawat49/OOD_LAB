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

print(" ***Cafe***")

# รับค่าและจัดการกับคำว่า "Log : " เผื่อในกรณีที่ก๊อปปี้มาวางทั้งหมด
raw_input = input("Log : ").strip()
if raw_input.startswith("Log : "):
    raw_input = raw_input[6:]
log = raw_input.split("/")

queue1 = Queue()
queue2 = Queue()

b1_free_time = 0
b2_free_time = 0

max_wait = 0
max_wait_cust = -1

for i in range(len(log)):
    ch = log[i].split(",")
    arr_time = int(ch[0])
    duration = int(ch[1])
    customer_id = i + 1
    
    # เลือกว่าบาริสต้าคนไหนจะว่างก่อน
    if b1_free_time <= b2_free_time:
        start_time = max(arr_time, b1_free_time)
        wait_time = start_time - arr_time
        end_time = start_time + duration
        b1_free_time = end_time
        # นำข้อมูลเข้าคิวของบาริสต้าคนที่ 1
        queue1.enqueue((end_time, customer_id))
    else:
        start_time = max(arr_time, b2_free_time)
        wait_time = start_time - arr_time
        end_time = start_time + duration
        b2_free_time = end_time
        # นำข้อมูลเข้าคิวของบาริสต้าคนที่ 2
        queue2.enqueue((end_time, customer_id))
        
    # หาคนที่รอนานที่สุด
    if wait_time > max_wait:
        max_wait = wait_time
        max_wait_cust = customer_id

# รวมผลลัพธ์จากทั้ง 2 คิวโดยดึง (Dequeue) คนที่ทำเสร็จก่อนออกมาพิมพ์เรียงตามลำดับเวลา
while not queue1.is_empty() or not queue2.is_empty():
    if not queue1.is_empty() and not queue2.is_empty():
        # ถ้ายังไม่ว่างทั้ง 2 คิว ให้ดูที่ตัวหน้าสุด (index 0)
        # queue1.queue[0][0] คือเวลา end_time ของคิวที่ 1
        if queue1.queue[0][0] < queue2.queue[0][0]:
            end_time, cust_id = queue1.dequeue()
            print(f"Time {end_time} customer {cust_id} get coffee")
        elif queue1.queue[0][0] > queue2.queue[0][0]:
            end_time, cust_id = queue2.dequeue()
            print(f"Time {end_time} customer {cust_id} get coffee")
        else:
            # ถ้าเสร็จพร้อมกัน ให้คนที่ customer_id น้อยกว่าได้ก่อน
            if queue1.queue[0][1] < queue2.queue[0][1]:
                end_time, cust_id = queue1.dequeue()
                print(f"Time {end_time} customer {cust_id} get coffee")
            else:
                end_time, cust_id = queue2.dequeue()
                print(f"Time {end_time} customer {cust_id} get coffee")
                
    # ถ้าเหลือแค่คิวเดียวแล้ว ก็ทะยอย Dequeue ออกมาได้เลย
    elif not queue1.is_empty():
        end_time, cust_id = queue1.dequeue()
        print(f"Time {end_time} customer {cust_id} get coffee")
    else:
        end_time, cust_id = queue2.dequeue()
        print(f"Time {end_time} customer {cust_id} get coffee")

# สรุปผลการรอคิว
if max_wait > 0:
    print(f"The customer who waited the longest is : {max_wait_cust}")
    print(f"The customer waited for {max_wait} minutes")
else:
    print("No waiting")