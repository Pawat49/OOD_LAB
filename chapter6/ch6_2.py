# นับจำนวนตัวอักษร
# input
# hello

# output
# h*e~l*~l*o
# 5
    

def length(txt):     
    #Code Here
    # base case ใช้ string จนหมด
    if txt == "":
        # print()
        # return 0 เมื่อใช้ตัวอักษรหมดแล้ว เพราะมีตัวอักษร 0 ตัว
        return 0

    # hell o 1 + 1
    # hel l~o* 1 + 2
    # he l*l~o* 1 + 3 
    # h e~l*l~o* 1 + 4
    # "" h*e~l*l~o* 0 + 5

    n = length(txt[:-1])
    # recursive case นับขนาดไปเรื่อยๆ ถ้าตอนนั้นเป็นเลขคู่เพิ่ม "*" ถ้าเป็นเลขคี่เพื่ม "~" แล้ว print ตัวอักษรนั้นพร้อมเครื่องหมายตามเงื่อนไข
    if n % 2 == 0:
        print(txt[-1]+"*",end="")
    else:
        print(txt[-1]+"~",end="")
    
    
    # return 1 + เรียกใช้ length อีกครั้งเพื่อเอาค่าที่ได้มา + กันเรื่อยๆ ก็จะได้ขนาดของ string ตอนนั้น
    return 1 + n # เอาตัวท้ายของ string ออกไปเรื่อยๆ ใช้ตัวอักษรที่เหลืออยู่เรียกใช้ recursive
a = length(input("Enter Input : "))
print("\n"+str(a))
#ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้)
