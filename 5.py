<<<<<<< HEAD
from  Q3 import factorial as m
=======
from Q3 import factorial as m
>>>>>>> c7791c941fd996a6ebf78bb2a41ee15944966e00
def compute(x):
    res =1
    chk =1
    for i in range(2,x+1,2):
        if chk%2==0:
            res+=(i/m(i))
        else:
            res-=(i/m(i))
        chk+=1
    return res
if __name__ == '__main__':
    n  =int(input("Enter the value of n : "))
    print(compute(n))
    