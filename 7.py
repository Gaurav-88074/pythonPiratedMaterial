
def menu():
    print("1.Find the length of a string")
    print("2.Return maximum of three string")
    print("3.Replace all vowel with #")
    print("4.find no. of words in a string")
    print("5.Palindrome or not?")

def choice():
    c = int(input("Enter your choice [1-5] :"))
    return c

def choice1():
    string = str(input("Enter the string : "))
    print(f"Length of {string} is : {len(string)}")

def choice2():
    string1 = str(input("Enter first  string : "))
    string2 = str(input("Enter second string : "))
    string3 = str(input("Enter third  string : "))
    l=[string1,string2,string3]
    res = string1
    for i in range(1,len(l)):
        if len(l[i])>len(res):
            res = l[i]
    print(f"maximum of three is : {res}")

def choice3():
    string = str(input("Enter string : "))
    l=list(string)
    for i in range(len(l)):
        if l[i] in ["a","i","e","o","u"]:
            l[i]="#"
    string  = "".join(l)
    print(string)

def choice4():
    string = str(input("Enter sentence : "))
    count = len(string.split(" "))
    print(count)

def choice5():
    string = str(input("Enter string : "))
    if string == string[::-1]:
        print("palindrome")
    else:
        print("Not palindrome!")

def line():
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    
def execute():
    line()
    menu()
    line()
    c=choice()
    if c==1:
        line()
        choice1()
        line()
        execute()
    elif c==2:
        line()
        choice2()
        line()
        execute()
    elif c==3:
        line()
        choice3()
        line()
        execute()
    elif c==4:
        line()
        choice4()
        line()
        execute()
    elif c==5:
        line()
        choice5()
        line()
        execute()
    else:
        return
execute()
