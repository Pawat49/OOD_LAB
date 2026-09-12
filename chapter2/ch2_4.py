# write function find sum that number 3 number sum equal 0 #
# not same in list
# len(array) >= 3
# if not have any number to sum equal 0 return []
# nC3
def three_sum(n):
    result = []

    if len(n) < 3:
        return f"Array Input Length Must More Than 2"
    
    for i in range(len(n) - 2):
        for j in range(len(n) - i - 2):
            for k in range(len(n) - i - j - 2):
                if int(n[i]) + int(n[i+j+1]) + int(n[i+j+k+2]) == 0 and [int(n[i]),int(n[i+j+1]),int(n[i+j+k+2])] not in result:
                    result.append([int(n[i]),int(n[i+j+1]),int(n[i+j+k+2])])

    return result

num_list = list(map(int,input("Enter Your List : ").split()))

print(three_sum(num_list))


