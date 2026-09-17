def bublesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
inp = input("Enter Input : ").split()
unsort_input = [int(i) for i in inp]
print(unsort_input)
print(bublesort(unsort_input))
