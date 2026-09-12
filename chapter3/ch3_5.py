class Stack():
    def __init__(self):
        self.stack = []
    def is_empty(self):
        if not self.stack:
            return True
        return False
    def push(self,data):
        self.stack.append(data)
        return self.stack
    def pop(self):
        if self.is_empty():
            return f"Empty"
        top = self.stack.pop()
        return top
    def peek(self):
        return self.stack[-1]
    def items(self):
        return len(self.stack)

def check_space(max,soi,operation,new):
    stack1 = Stack()
    stack2 = Stack()
    for i in soi.split(","):
        stack1.push(int(i))
    if 0 in stack1.stack:
        stack1.stack = []
    if operation == "arrive":
        if stack1.items() >= max:
            return f"car {new} cannot arrive : Soi Full\n{stack1.stack}"
        if int(new) in stack1.stack:
            return f"car {new} already in soi\n{stack1.stack}"
        stack1.push(new)
        return f"car {new} arrive! : Add Car {new}\n{stack1.stack}"
    elif operation == "depart":
        if stack1.is_empty():
            return f"car {new} cannot depart : Soi Empty\n{stack1.stack}"
        if int(new) not in stack1.stack:
            return f"car {new} cannot depart : Dont Have Car {new}\n{stack1.stack}"
        while int(stack1.peek()) != int(new) and not stack1.is_empty():
            top = stack1.pop()
            stack2.push(top)
        return f"car {new} depart ! : Car {new} was remove\n{stack2.stack[::-1]}"
        

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()

m,n = int(m),int(n)
### Enter Your Code Here ###

# print(f"m = {m} | s = {s} | o = {o} | n = {n}")

print(check_space(m,s,o,n))


