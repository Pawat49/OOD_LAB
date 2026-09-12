

class Stack:

    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)
        return self.stack

    def pop(self):
        top_ch = self.stack.pop()
        return top_ch

    def is_empty(self):
        if not self.stack:
            return True
        return False

bracket = input("Enter Input : ")


def check_Parentheses(b):
    stack = Stack()
    pairs = {")":"(","]":"[","}":"{"}
    for i in b:
            if i in "([{":                
                stack.push(i)
            elif i in "}])":
                if stack.is_empty():
                    return False
                top = stack.pop()
                if top != pairs[i]:
                    return False
            else:
                return False
    return len(stack.stack) == 0
if check_Parentheses(bracket):
    print(f"Parentheses : Matched ! ! !")
else:
    print(f"Parentheses : Unmatched ! ! !")





