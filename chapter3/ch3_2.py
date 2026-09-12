class Stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
        return self.stack
    def pop(self):
        if self.is_empty():
            return f"Empty"
        top = self.stack.pop()
        return top
    def is_empty(self):
        if not self.stack:
            return True
        return False
    def peek(self):
        if self.is_empty():
            return f"Empty"
        return self.stack[-1]
    def item(self):
        return len(self.stack)
c = input("Enter Input : ").split(",")
# print(c)

a = Stack()
w_f_list = []
for i in c:
    w_f_list.append(i.split())
# print(w_f_list)

# print(a.stack)
# print(a.peek())
for i in range(len(w_f_list)):
    while not a.is_empty() and int(a.peek()[0]) < int(w_f_list[i][0]):
        
        f = a.pop()
        print(f[1])
        # print(f"peek = {a.peek()}")
    
    a.push(w_f_list[i])
    
    
            
# print(a.stack)
        



