def print1ToN(n):
    # n = 5
    # 5
    # printNto1(4)
    # 4
    # printNto1(3)
    # 3
    # printNto1(2)
    # 2
    # printNto1(1)
    # 1
    # 2
    # 3
    # 4
    # 5
    if n <= 0:
        print(1,end=" ")
        return
    elif n == 1:
        print(1,end=" ")
        return
    
    # recursive case
    print1ToN(n - 1)
    print(n,end =" ")
    
# print1ToN(1)
def printNto1(n):
    # n = 5
    # 5
    # printNto1(4)
    # 4
    # printNto1(3)
    # 3
    # printNto1(2)
    # 2
    # printNto1(1)
    if n <= 1:
        print(1,end=" ")
        return
    print(n,end=" ")
    return printNto1(n-1)

n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)
