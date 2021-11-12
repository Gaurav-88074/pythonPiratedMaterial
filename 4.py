def computeDigit(n):
    if n==0:
        return 0
    else:
        return computeDigit(n//10)+1
userInput = int(input("Enter the number : "))
print(f"{computeDigit(userInput)} digits present")