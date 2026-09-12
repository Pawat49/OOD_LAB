def mod_position(arr, s):
    mod_pos_str = [arr[i] for i in range(len(arr)) if (i + 1) % int(s) == 0]
    return mod_pos_str

print("*** Mod Position ***")

string,num = input("Enter Input : ").split(",")[:2]
print(mod_position(string,int(num)))
