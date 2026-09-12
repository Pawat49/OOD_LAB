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

def check_duplicate(q):
    for i in range(len(q)):
        j = i + 1 
        while j < len(q):
            if q[i] == q[j]:
                return f"Duplicate"
            j += 1
    return f"NO Duplicate"

shelf,book = input("Enter Input : ").split("/")

book = book.split(",")
queue = Queue()

for i in shelf.split():
    queue.enqueue(i)


for i in range(len(book)):
    c = book[i].split()
    if c[0] == "D":
        queue.dequeue()
    elif c[0] == "E":
        queue.enqueue(c[1])
print(check_duplicate(queue.queue))

