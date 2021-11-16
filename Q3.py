def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-2)+fibo(n-1)
def factorial(n):
    if n<=0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
def factorialOfFiboSequence(sequence,result=[],i=0):
    if i==len(sequence):
        return result
    else:
        result.append(factorial(sequence[i]))
        return factorialOfFiboSequence(sequence,result,i+1)
def fabonaciiSeries(range,result=[],i=0):
    if i==range:
        return result
    else:
        result.append(fibo(i))
        return fabonaciiSeries(range,result,i+1)
if __name__ == '__main__':
    
    userInput = int(input("Enter the range : "))
    fiboList = fabonaciiSeries(userInput+1)
    print(f"Fibonacii Sequence : {fiboList}")
    factList = factorialOfFiboSequence(fiboList)
    print(f"Factorial Sequence : {factList}")
