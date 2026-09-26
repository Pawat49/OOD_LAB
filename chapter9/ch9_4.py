# Input มี 2 ส่วน คือ คำที่ต้องการเรียงลำดับ และรูปแบบการเรียง

# รูปแบบการเรียง

# W (Weight) : เรียงตามน้ำหนักของคำจากน้อยไปมาก โดยน้ำหนักคำนวณจากผลรวมของตัวอักษรทั้งหมด a = 1, b = 2 … z = 26
# W = cat(24) dog(26) banana(33) fish(42) grape(47) mango(50) apple(50) zebra(52)
# V (Vowel) : เรียงตามจำนวนสระในแต่ละคำจากน้อยไปมาก หากจำนวนสระเท่ากันจะใช้สระที่มี priority สูงสุดในคำเป็นตัวตัดสินเรียงลำดับ โดยใช้เกณฑ์ a > e > i > o > u
# V = mars(1)(a) sun(1)(u) earth(2)(a,e) saturn(2)(a,u) venus(2)(e,u) mercury(2)(e,u) moon(2)(o,o) pluto(2)(o,u) jupiter(3)(e,i,u) neptune(3)(e,e,u)
def selectionsort(word_arr,m):
    n = len(word_arr)
    if m == "W":
        for last in range(n-1,0,-1):
            big_i = 0
            for i in range(1,last+1):
                if word_arr[big_i][1] > word_arr[i][1]:
                    big_i = i
                elif word_arr[big_i][1] == word_arr[i][1]:
                    if word_arr[big_i][2] > word_arr[i][2]:
                        big_i = i
            word_arr[big_i],word_arr[last] = word_arr[last],word_arr[big_i]
    elif m == "V":
        for last in range(n-1,0,-1):
            big_i = 0
            for i in range(1,last+1):
                if word_arr[big_i][1] > word_arr[i][1]:
                    big_i = i
                elif word_arr[big_i][1] == word_arr[i][1]:
                    if word_arr[big_i][2] > word_arr[i][2]:
                        big_i = i
                    elif word_arr[big_i][2] == word_arr[i][2]:
                        if word_arr[big_i][3] > word_arr[i][3]:   # เดิมคือ len(...) > len(...)
                            big_i = i
            word_arr[big_i],word_arr[last] = word_arr[last],word_arr[big_i]
    return word_arr
def weight_word(word_jaa):
    weight = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10
        ,'k': 11,'l': 12,'m':13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20
        ,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26}
    vowel = {'a': 5,'e': 4,'i': 3,'o': 2,'u': 1}
    val_weight = 0
    val_vowel = 0
    for w in word_jaa:
        val_weight += weight[w]
        if w in vowel.keys():
            val_vowel += vowel[w]
    return word_jaa,val_weight,val_vowel
def vowel_word(word_jaa, order):
    weight = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10
        ,'k': 11,'l': 12,'m':13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20
        ,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26}
    vowel = {'a': 1,'e': 2,'i': 3,'o': 4,'u': 5}
    vowel_in_word = 0
    val_vowel = 0
    for w in word_jaa:
        if w in vowel.keys():
            vowel_in_word += 1
            if val_vowel == 0 or vowel[w] < val_vowel:   # เก็บสระที่ค่าน้อยสุด (priority สูงสุด)
                val_vowel = vowel[w]
    return word_jaa,vowel_in_word,val_vowel,order
print("***Fun with Word***")
inp = input("Enter Input : ").split("/")
# print(inp)
word = inp[0].split()
mode = inp[1]
# print(word,mode)
word_with_weight = []
if mode == "W":
    for w in word:
        weight_w = weight_word(w)
        word_with_weight.append(weight_w)
    # print(word_with_weight)
    sort_word_with_weight = selectionsort(word_with_weight,mode)
    # print(sort_word_with_weight)
    n = len(sort_word_with_weight)
    for i in sort_word_with_weight[-1::-1]:
        print(i[0],end=" ")
elif mode == "V":
    for w in word:
        weight_w = vowel_word(w, len(word_with_weight))   # len ตอนนี้ = ลำดับที่กำลังจะ append
        word_with_weight.append(weight_w)
    # print(word_with_weight)
    sort_word_with_weight = selectionsort(word_with_weight,mode)
    # print(sort_word_with_weight)
    n = len(sort_word_with_weight)
    for i in sort_word_with_weight[-1::-1]:
        print(i[0],end=" ")
