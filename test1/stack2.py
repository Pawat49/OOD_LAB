class Stack():
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.is_empty():
            return
        top = self.stack.pop()
        return top
    def is_empty(self):
        if self.stack == []:
            return "Empty"
        return
    def peek(self):
        if self.is_empty():
            return
        return self.stack[-1]
    def size(self):
        return len(self.stack)
def check(p):
    s = Stack()
    for i in p:
        if i == "(":
            s.push(i)
        elif i == ")":
            if s.is_empty():
                return False
            s.pop()
        else:
            continue
    return s.size() == 0 
inp = input("Enter input : ")
print(inp)
if check(inp):
    print("true")
else:
    print("false")


