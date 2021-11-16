def computeDigit(n,s):
    if n==0:
        return s
    else:
        s.add(n%10)
        return computeDigit(n//10,s)
Set = set()
userInput = int(input("Enter the number : "))
print(f"{computeDigit(userInput,Set)}")