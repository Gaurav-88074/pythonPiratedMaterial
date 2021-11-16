def insertDetails(obj, name, marks):
    obj[name] = marks

def userInput(obj):
    marks = list()
    name  = str(input("Enter the name of student : "))
    for i in range(4):
        value = int(input(f"Enter marks of subject {i+1} : "))
        marks.append(value)
    insertDetails(obj,name,marks)
    print()
def getMax(obj,maxValue):
    print()
    for i in obj:
        if sum(obj[i])==maxValue:
            return i
def display(obj):
    maxValue = 0
    for i in obj:
        print(f"{i} : {obj[i]} : {sum(obj[i])}")
        maxValue = max(maxValue,sum(obj[i]))
    return maxValue
if __name__ == '__main__':
    obj = dict()
    for i in range(2):
        userInput(obj)
    maxValue = display(obj)
    name = getMax(obj,maxValue);
    print(f"{name} [securing highest percentage]")
    


    