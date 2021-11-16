from  Q3 import factorial as m
def compute(x):
    res =1
    chk =1
    for i in range(2,x+1,2):
        res+=(i/m(i))*((-1)**i)
       
    return res
if __name__ == '__main__':
    n  =int(input("Enter the value of n : "))
    print(compute(n))
    