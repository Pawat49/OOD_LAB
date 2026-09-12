# input 3
# output __#
#        _##
#        ###
# 
# input -3
# output  ###
#         _##
#         __#

def staircase(n,current=0):
    #code here

    # error case
    if n == 0:
        print("Not Draw!")
        return

    # staircase(1,2) string = __#
    # staircase(2,1) string = _##
    # staircase(3)   string = ###
    
    
    
    if n > 0:
        # base case n > 0
        if n == 1:
            string = "_"*current + "#"*n + "\n"
            print(string,end="")
            return
        # recursivee case n > 0
        staircase(n-1,current+1)
        string = "_"*current + "#"*n + "\n"
        print(string,end="")
    if n < 0:
        # base case n < 0
        if n == -1:
            string = "_"*(abs(n) - 1) + "#"*(current+1) + "\n"
            print(string,end="")
            return
        # recursivee case n < 0
        staircase(n+1,current+1)
        string = "_"*(abs(n) - 1) + "#"*(current+1) + "\n"
        print(string,end="")

staircase(int(input("Enter Input : ")))
# number = int(input("Enter input : "))
# for i in range(number):
#     for j in range(number):
#         if i + j >= number - 1:
#             print("#",end="")
#         else:
#             print("_",end="")
#     print()
