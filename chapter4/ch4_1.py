class Queue():
    def __init__(self):
        self.queue = []
    def is_empty(self):
        if self.queue:
            return False
        return True
    def sizes(self):
        return len(self.queue)
    def enqueue(self,data):
        self.queue.append(data)
        return self.queue
    def dequeue(self):
        if self.is_empty():
            return "Empty"
        first = self.queue.pop(0)
        return first
    
def queue_func(ch):
    queue = Queue()

    for i in range(len(ch)):
        char = c[i].split()
        # print(ch)
        if char[0] == "E":
            queue.enqueue(char[1])
            # print(f"queue = {queue.queue}")
            print(queue.sizes())
        elif char[0] == "D":
            if queue.is_empty():
                print(f"{-1}")
                continue

            first = queue.queue[0]
            index = queue.queue.index(first)
            
            print(f"{first} {index}")
            queue.dequeue()
            
        
    if queue.is_empty():
        print(f"Empty")
        return
    for i in queue.queue:
        print(i,end=" ")
    print()

c = input("Enter Input : ").split(",")
# print(c)
queue_func(c)
