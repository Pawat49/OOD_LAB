def bublesort(arr,n,i=0,j=0):
    if i == n - 1:
        return arr
    if j == n - i - 1:
        return bublesort(arr,n,i+1,0)
    if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
    return bublesort(arr,n,i,j+1)
inp = input("Enter Input : ").split()
unsort_input = [int(i) for i in inp]
# print(unsort_input)
print(bublesort(unsort_input,len(unsort_input)))
