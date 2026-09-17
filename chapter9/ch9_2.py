def strightselectionsort(arr,last,i=1,big_i=0):
    if last == 1:
        if arr[big_i] > arr[last]:
        
            arr[last],arr[big_i] = arr[big_i],arr[last]
            print(f"swap {arr[big_i]} <-> {arr[last]} : {arr}")
            
        return arr

    if i == last:
        if arr[big_i] > arr[last]:

            arr[last],arr[big_i] = arr[big_i],arr[last]
            print(f"swap {arr[big_i]} <-> {arr[last]} : {arr}")

        return strightselectionsort(arr,last-1,1,0)
    
    if arr[i] > arr[big_i]:
        big_i = i

    return strightselectionsort(arr,last,i+1,big_i)

inp = input("Enter Input : ").split()
unsort_arr = [int(i) for i in inp]
# print(unsort_arr)
print(strightselectionsort(unsort_arr,len(unsort_arr)-1))