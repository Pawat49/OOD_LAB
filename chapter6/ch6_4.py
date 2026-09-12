# เปรี้ยวลัพธ์ = เปรี้ยวทุกอันคูณกัน
# ขมลัพธ์ = ขมทุกอันบวกกัน
# ต้องลองหาขมลัพธ์กับเปรี้ยวลัพธ์ตั้งแต่ส่วนผสม 1 ชนิด ถึง n ชนิด
# โจทย์ จงเขียนโปรแกรมเพื่อหาค่าผลต่างของความเปรี้ยวลัพธ์และความขมลัพธ์ของส่วนผสม ที่น้อยที่สุด |s - b|

def sum(l):
    if len(l) == 1: 
        return int(l[0])
    return sum(l[1:]) + int(l[0])

def product(l):
    if len(l) == 1:
        return int(l[0])
    return product(l[1:]) * int(l[0])



def perket(p,product=1,sum=0,index=0,count=0):
    # ถ้าเช็คครบแล้วและหาค่าminได้ minหาไปเรื่อยๆอยู่แล้ว

    # base case
    if index == len(p):
        if count == 0:
            return 100000000
        return abs(product - sum)

    # recursive case
    a = perket(p,product,sum,index+1,count)
    b = perket(p,product*int(p[index][0]),sum+int(p[index][1]),index+1,count+1)
    return min(a,b)
    
# testcase2
# input 3 8,5 8
# perket([[3,8],[5,8]])
# index == 0
# a = perket([[3,8],[5,8]],product=1,sum=0,index+1,count=0)
# a -> return 100000000
# b = perket([[3,8],[5,8]],product*3,sum+8,index+1,count=1)
# return min(100000000,5) -> 5
# index == 1
# a = perket([[3,8],[5,8]],product=1,sum=0,index+1,count=0)
# b = perket([[3,8],[5,8]],product*3,sum+8,index+1,count=1)
    

inp = input("Enter Input : ").split(",")

sour = []
bitter = []
perket_jaa = []

for i in inp:
    i = i.split()
    sour.append(i[0])
    bitter.append(i[1])
    perket_jaa.append(i)

# print(f"inp = {inp} | perket_jaa = {perket_jaa} | sour = {sour} | bitter = {bitter}")
# print(product(perket_jaa[0][0]))
print(perket(perket_jaa))


