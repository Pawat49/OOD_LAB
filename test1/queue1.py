class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if self.is_empty():
            return
        front = self.queue.pop(0)
        return front
    def is_empty(self):
        if self.queue == []:
            return None
        return
    def front(self):
        if self.size() == 0:
            return "None"
        return self.queue[0]
    def size(self):
        return len(self.queue)


def shop(n):
    q = Queue()
    count = []
    for i in range(n):
        inp = input().split()
        if inp[0] == "SIZE":
            count.append(q.size())
        elif inp[0] == "ENQUEUE":
            q.enqueue(inp[1])
        elif inp[0] == "DEQUEUE":
            q.dequeue()

    for c in count:
        print(c)
    return f"Remaining: {q.size()} person, front: {q.front()}"
num = int(input())

print(shop(num))
