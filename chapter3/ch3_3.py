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
    
# def show(s):
#     print(len(s))
#     if len(s) == 0:
#         print("Empty")
#     for i in s[::-1]:
#         print(i,end="")
#     print()
#     if combo >= 2:
#         print(f"Combo : {combo} ! ! !")
ch = input("Enter Input : ").split()
stack1 = Stack()
combo = 0


# a b a b a
for i in range(len(ch)):
    stack1.push(ch[i])
    if i > 1:
        count = 0
        for j in stack1.stack[::-1]:
            if j == stack1.peek():
                count += 1
            else:
                break
        if count == 3:
            while stack1.peek() == ch[i]:
                
                stack1.pop()

            combo += 1
        

# show(stack.stack)

# ch[i]*3 == ch[i:i+3]
print(len(stack1.stack))
if len(stack1.stack) == 0:
    print("Empty",end="")
for i in stack1.stack[::-1]:
    print(i,end="")
if combo >= 2:
    print(f"\nCombo : {combo} ! ! !")

