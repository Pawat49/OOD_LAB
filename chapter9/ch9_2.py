def strightselectionsort(arr):
    
    n = len(arr)
    for last in range(n-1,0,-1):
        big_i = 0
        for i in range(1,last+1):
            if arr[i] > arr[big_i]:
                big_i = i
        arr[last],arr[big_i] = arr[big_i],arr[last]
        if arr[last] != arr[big_i]:
            print(f"swap {arr[big_i]} <-> {arr[last]} : {arr}")
    return arr

inp = input("Enter Input : ").split()
unsort_arr = [int(i) for i in inp]
print(unsort_arr)
print(strightselectionsort(unsort_arr))