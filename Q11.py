def linearSearch(array,key,index = 0):
    if index==len(array):
        return -1
    elif key==array[index]:
        return index
    else:
        return linearSearch(array,key,index+1)
        
def binarySearch(array,key,start,end):
    mid = (start+end)//2
    if start>end : 
        return -1
    elif array[mid] == key:
        return mid
    elif key<array[mid]:
        return binarySearch(array,key,start,mid-1)
    else:
        return binarySearch(array,key,mid+1,end)
def bubbleSort(array):
    for i in range(len(array)):
        print("Iteration :",i+1)
        print(array)
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
def ssort(A):
    for i in range(len(A)):
        min_= i
        for j in range(i+1, len(A)):
            if A[min_] > A[j]:
                min_ = j
                A[i], A[min_] = A[min_], A[i]
def isort(list1):
    
    for i in range(1, len(list1)):
        value = list1[i]
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
            if(ch==1):
                str1 = input("enter the name  :")
                print(f"Element found at index : {linearSearch(Lname,str1)}")
            elif(ch==2):
                str1 = input("enter the name  :")
                print(f"Element found at index : {binarySearch(Lname,str1)}")
                binarySearch(Lname,str1)
            else:
                print("Enter Valid choice")
        elif(ch==2):
            print("1. Bubble Sort")
            print("2. Insertion Sort")
            print("3. Selection Sort")
            ch3=int(input("Enter your choice : "))
            if (ch3 == 1):
                bubbleSort(Lname)
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

if __name__ == '__main__':
    
    studentName = []
    size = int(input("How many students ? : "))
    for i  in range(size):
        sName = str(input(f"Enter name of student : {i+1}"))
        studentName.append(sName)
    menu(studentName)