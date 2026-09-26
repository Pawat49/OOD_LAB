# รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก 1234 และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก 12344 และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย 4321 และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"

# - หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย 43211 และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"

# - หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด 5555 ให้แสดงผลว่า "Repdrome"

# - หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า 1243 "Nondrome"

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
inp = input("Enter Input : ")
n = len(inp)

increase = False
decrease = False
equal = False

for i in range(n - 1):
    if inp[i] < inp[i+1]:
        increase = True
    elif inp[i] > inp[i+1]:
        decrease = True
    else:
        equal = True

if not increase and not decrease:
    print("Repdrome")
elif increase and decrease:
    print("Nondrome")
elif increase:
    if equal:
        print("Plaindrome")
    else:
        print("Metadrome")
else:
    if equal:
        print("Nialpdrome")
    else:
        print("Katadrome")
