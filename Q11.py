'''
11.Write a menu-driven program to accept a list of student names and perform the following

a.search an element using linear search/binary search.
b.Sort the elements using bubblesort/insertionsort/selectionsort.
'''
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
                
if __name__ == '__main__':
    size = int(input("Enter size of list : "))
    array = list()
    for i in range(size):
        value = int(input(f"Enter element {i+1} : "))
        array.append(value)
    linearSearch(array,0)
    print("element fount at index at ",linearSearch(array,7))
    print(array)
    bubbleSort(array)
    print(array)

    
