import math
def compute(x):
    res =1
    chk =1
    for i in range(2,x+1,2):
        if chk%2==0:
            res+=(i/math.factorial(i))
        else:
            res-=(i/math.factorial(i))
        chk+=1
    return res
if __name__ == '__main__':
    n  =int(input("Enter the value of n : "))
    print(compute(n))
    