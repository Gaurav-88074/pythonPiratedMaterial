# fibonacci series: 0 1 1 2 3 5 8 13 _ _ _
def fiboAndFact(n):
    if n == 1:          # n=1 means 1st term of fibonacci series i.e 0
        return [0, 1]   # 0! = 1
    if n == 2:
        return [1, 1]   # 2nd term = 1, 1! = 1
    else:
        fact = fiboAndFact(n-2)[0] + fiboAndFact(n-1)[0]
        return [fact, factorial(fact)]


def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

if __name__ == '__main__':

    n = int(input("Enter value of n: "))
    [fib, fact] = fiboAndFact(n)
    print("Nth Fibonacci Term: {0}\nFactorial of Nth Term: {1}".format(fib, fact))
