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
# i = 0 j = 0 [4 3 2 1]
# i = 0 j = 1 [3 4 2 1]
# i = 0 j = 2 [3 2 4 1]
# i = 0 j = 3 [3 2 1 4]
# i = 1 j = 0 [3 2 1 4]
# i = 1 j = 1 [2 3 1 4]
# i = 1 j = 2 [2 1 3 4]
# i = 2 j = 0 [2 1 3 4]
# i = 2 j = 1 [1 2 3 4]
# i = 3 return [1 2 3 4]