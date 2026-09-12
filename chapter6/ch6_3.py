def parenthesis(n,open = 0,close = 0,current = ""):
    # base case
    if open == n and close == n:
        return [current]

    result = []
    # recursive case
    if open < n:
        result = result + parenthesis(n,open+1,close,current + "(")
    if close < open:
        result = result + parenthesis(n,open,close+1,current + ")")
    return result
    
num = int(input("Enter number of pair parenthesis(es): "))
print("All possible parenthesis(es)")
print(",".join(parenthesis(num)))
