n = input("Enter : ").split()
print(n)

for i in range (len(n)):
    if n[i] == "VISIT":
        print("visit")
        
    elif n[i] == "BACK":
        print("back")
    elif n[i] == "FORWARD":
        print("forward")
    elif n[i] == "CURRENT":
        print("current")
    elif n[i] == "HISTORY":
        print("history")
    elif n[i] == "REMOVE":
        print("remove")
    elif n[i] == "CLEAR":
        print("clear")
    elif n[i] == "END":
        print("end")
    else:
        print("page and int")
