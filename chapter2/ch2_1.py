class Calculator :

    ### Enter Your Code Here ###

    def __init__(self,num):
        self.num = num

    def __add__(self,other):
        if isinstance(other,int):
            return self.num + other
        return self.num + other.num
        ###Enter Your Code For Add Number###

    def __sub__(self,other):
        if isinstance(other,int):
            return self.num - other
        return self.num - other.num
        ###Enter Your Code For Sub Number### 

    def __mul__(self,other):
        if isinstance(other,int):
            return self.num * other
        return self.num * other.num
        ###Enter Your Code For Mul Number###

    def __truediv__(self,other):
        if isinstance(other,int):
            return self.num / other
        return self.num / other.num
        ###Enter Your Code For Div Number###

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")
