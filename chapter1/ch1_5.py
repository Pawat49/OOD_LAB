n = int(input("Enter Input : "))
# 2*n + 4

# top
for i in range(n + 2):
    for j in range(2 * n + 4):
        if j < n + 2:
            if i + j >= n + 1:
                print("#",end="")
            else:
                print(".",end="")

        if j >= n + 2:
            if (i == 0 or i == n + 1) or (j == n + 2 or j == 2 * n + 3):
                print("+",end="")
            else:
                print("#",end="")
    print()

# under
for i in range(n + 2):
    for j in range(2 * n + 4):
        if j < n + 2:
            if (i == 0 or i == n + 1) or (j == 0 or j == n + 1):
                print("#",end="")
            else:
                print("+",end="")
        
        if j >= n + 2:
            if i + j <= 2 * n + 3:
                print("+",end="")
            else:
                print(".",end="")
    print()

# for i in range(n + 2):
#     for j in range(n + 2):
#         if i + j >= n + 1:
#             print("#",end="")
#         else:
#             print(".",end="")
#     print()

# for i in range(n + 2):
#     for j in range(n + 2):
#         if (i == 0 or i == n + 1) or (j == 0 or j == n + 1):
#             print("+",end="")
#         else:
#             print("#",end="")
#     print()

# for i in range(n + 2):
#     for j in range(n + 2):
#         if (i == 0 or i == n + 1) or (j == 0 or j == n + 1):
#             print("#",end="")
#         else:
#             print("+",end="")
#     print()

# for i in range(n + 2):
#     for j in range(n + 2):
#         if i + j <= n + 1:
#             print("+",end="")
#         else:
#             print(".",end="")
#     print()
