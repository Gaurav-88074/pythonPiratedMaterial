
def lsearch(L,str):
    for item in L:
        if(item==str):
            print("Element is present in the List")
            return
    print("Element is not present in the List")
def bsearch(L,str):
    L.sort()
    llen= len(L)-1
    i=0
    while(i<=llen):
        m=(i+(llen-1))/2
        res=-1000
        if(str==L[m]):
            res=0
            if(res==0):
                return m
        if(str>L[m]):
            i=m+1
        else:
            i=m-1
    return False

def bsort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j]>list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1

def isort(list1):
    # Outer loop to traverse through 1 to len(list1)
    for i in range(1, len(list1)):
        value = list1[i]
        # Move elements of list1[0..i-1], that are
        #greater than value, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
            list1[j + 1] = value
    return list1



def menu(Lname):
    while(True):
        print("Enter your choice :")
        print("1. Search an Element.")
        print("2. Sort the elements")
        ch=int(input("Enter your choice : "))
        if(ch==1):
            print("1. Linear Search")
            print("2. Binary Search")
            ch2=int(input("Enter your choice : "))
            str=input("Enter the element : ")
            if(ch==1):
                lsearch(Lname,str)
            elif(ch==2):
                bsearch(Lname,str)
            else:
                print("Enter Valid choice")
        elif(ch==2):
            print("1. Bubble Sort")
            print("2. Insertion Sort")
            print("3. Selection Sort")
            ch3=int(input("Enter your choice : "))
            if (ch3 == 1):
                Lname=bsort(Lname)
                print(Lname)
            elif (ch3 == 2):
                Lname=isort(Lname)
                print(Lname)
            elif(ch3 == 3):
                Lname=ssort(Lname)
                print(Lname)
            else:
                print("Enter Valid choice")
        elif(ch==3):
            break
        else:
            print("Enter a Valid Choice!")

def ssort(A):
    for i in range(len(A)):
        min_= i
        for j in range(i+1, len(A)):
            if A[min_] > A[j]:
                min_ = j
                A[i], A[min_] = A[min_], A[i]
    return A

Lname=[]
inputn=" "
while(inputn!=""):
    inputn=input("Enter the name : ")
    if(inputn!=""):
        Lname.append(inputn)
menu(Lname)