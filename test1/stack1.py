class Stack():
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
        return
    def pop(self):
        if self.is_empty():
            return
        top = self.stack.pop()
        return top
    def peek(self):
        if self.is_empty():
            return
        return self.stack[-1]
    def is_empty(self):
        if self.stack == []:
            return "Blank Page"
        return
    def size(self):
        return len(self.stack)
def backward(web):
    stack = Stack()
    for w in web:
        if w == "BACK":
            stack.pop()
        else:
            stack.push(w)
    if stack.is_empty():
        return stack.is_empty()
    return stack.peek()

website = input("Enter input : ").split(",")
print(backward(website))


