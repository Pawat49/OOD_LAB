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

def main():
    # 1. รับค่า Input
    try:
        user_input = input("Enter width, height, and room: ").split()
        if len(user_input) != 3:
            print("Invalid map input.")
            return
    except:
        return

    width = int(user_input[0])
    height = int(user_input[1])
    room = user_input[2]
    
    r = room.split(",")

    # 2. ตรวจสอบความถูกต้องของแผนที่ (Validation - Testcase #3, #4)
    if len(r) != height:
        print("Invalid map input.")
        return
        
    for row in r:
        if len(row) != width:
            print("Invalid map input.")
            return
            
    # หาพิกัดเริ่มต้น 'F'
    start = None
    for i in range(height):
        for j in range(width):
            if r[i][j] == "F":
                start = (j, i)
                break
        if start:
            break
            
    # ถ้าไม่มี 'F' ในแมพ
    if not start:
        print("Invalid map input.")
        return

    # 3. เตรียมพร้อม Queue และตัวแปร BFS
    queue = Queue()
    visited = Queue()
    
    queue.enqueue(start)
    visited.enqueue(start)
    
    # พิมพ์สถานะคิวรอบแรก (จุดเริ่มต้น)
    print(f"Queue: {queue.queue}")
    
    found_exit = False
    
    # 4. เริ่มประมวลผล BFS
    while not queue.is_empty():
        step = queue.dequeue()
        step_x = step[0]
        step_y = step[1]
        
        # ลำดับทิศทาง: เหนือ (-y), ออก (+x), ใต้ (+y), ตก (-x)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for dy, dx in directions:
            next_y = step_y + dy
            next_x = step_x + dx
            
            # เช็คว่าอยู่ในขอบเขต Map
            if 0 <= next_x < width and 0 <= next_y < height:
                # เช็คว่ายังไม่เคยเดินผ่าน
                if (next_x, next_y) not in visited.queue:
                    # ถ้าช่องถัดไปคือทางออก
                    if r[next_y][next_x] == "O":
                        print("Found the exit portal.")
                        found_exit = True
                        break
                    
                    # ถ้าช่องถัดไปคือทางเดินปกติ
                    elif r[next_y][next_x] == "_":
                        visited.enqueue((next_x, next_y))
                        queue.enqueue((next_x, next_y))
                        
        # หยุดการทำงานของ While Loop ทันทีถ้าเจอทางออกแล้ว
        if found_exit:
            break
            
        # พิมพ์สถานะ Queue ณ ปัจจุบันหลังจากเช็คครบ 4 ทิศทาง
        # (เงื่อนไขไม่ให้พิมพ์คิวว่างตาม Testcase #5)
        if not queue.is_empty():
            print(f"Queue: {queue.queue}")

    # 5. กรณีคิวถูกประมวลผลจนหมดแล้วแต่ยังไม่เจอ 'O'
    if not found_exit:
        print("Cannot reach the exit portal.")

# เริ่มการทำงานของโปรแกรม
if __name__ == "__main__":
    main()