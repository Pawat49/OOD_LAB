class Stack():
    def __init__(self):
        self.stack = []
    def is_empty(self):
        if not self.stack:
            return True
        return False
    def push(self,data):
        if not isinstance(data,int):
            return f"Invalid instruction: {data}"
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

class StackCalc():
    def __init__(self):
        self.operand = Stack()
        self.error_msg = ""
    def run(self,arg):
        
        for i in arg:
            result = 0
            if not i.isdigit() and i not in ["+","-","*","/","DUP","POP","PSH"]:
                self.error_msg = f"Invalid instruction: {i}"
                return self.error_msg

            if i == "+":
                top = self.operand.pop()
                result = top + self.operand.peek()
                # print(f"top = {top} | result = {result} | peek = {self.operand.peek()}")
                self.operand.pop()
                self.operand.push(result)
            elif i == "-":
                top = self.operand.pop()
                result = top - self.operand.peek()
                # print(f"top = {top} | result = {result} | peek = {self.operand.peek()}")
                self.operand.pop()
                self.operand.push(result)
            elif i == "*":
                top = self.operand.pop()
                result = top * self.operand.peek()
                # print(f"top = {top} | result = {result} | peek = {self.operand.peek()}")
                self.operand.pop()
                self.operand.push(result)
            elif i == "/":
                top = self.operand.pop()
                result = top / self.operand.peek() 
                # print(f"top = {top} | result = {result} | peek = {self.operand.peek()}")
                self.operand.pop()
                self.operand.push(int(result))
            elif i == "DUP":
                top = self.operand.peek()
                self.operand.push(top)
            elif i == "POP":
                self.operand.pop()
            elif isinstance(int(i),int):
                self.operand.push(int(i))
    def getValue(self):
        if self.error_msg:
            return self.error_msg

        if self.operand.is_empty():
            return 0
        
        return int(self.operand.peek())
        

print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)

print(machine.getValue())