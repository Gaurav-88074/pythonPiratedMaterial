from Q3 import factorial

def compute(x, n):
    result = 0
    for i in range(1, n+1):
        m = i-1
        result = result + ((((-1)**m) * (x**(2*m)))/factorial(2*m))
    return result


if __name__ == '__main__':
    n = int(input("Enter the value of n : "))
    x = int(input("Enter value of x: "))
    print(compute(x, n))
