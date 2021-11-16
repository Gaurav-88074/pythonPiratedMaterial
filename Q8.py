def menu():
    print("1.To check all elemnts are numbers")
    print("2.Count number of numeric value")
    print("3.Display largest string")
    print("4.Display list in reverse form")
    print("5.Find specific element in element")
    print("6.Remove specific element in element")
    print("7.sort list in descending order ")
    print("8.Accept two list and find comment elements")


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
    l = [string1, string2, string3]
    res = string1
    for i in range(1, len(l)):
        if len(l[i]) > len(res):
            res = l[i]
    print(f"maximum of three is : {res}")


def choice3():
    string = str(input("Enter string : "))
    l = list(string)
    for i in range(len(l)):
        if l[i] in ["a", "i", "e", "o", "u"]:
            l[i] = "#"
    string = "".join(l)
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
    c = choice()
    if c == 1:
        line()
<<<<<<< HEAD
        choice1()
        line()
        execute()
    elif c == 2:
        line()
        choice2()
        line()
        execute()
    elif c == 3:
        line()
        choice3()
        line()
        execute()
    elif c == 4:
        line()
        choice4()
        line()
        execute()
    elif c == 5:
        line()
        choice5()
        line()
        execute()
    else:
        return


execute()
=======
        chk = choice1(List)
        if chk:
            choice2(List)
        line()
        execute(List)
    elif c == 2:
        line()
        choice2(List)
        line()
        execute(List)
    elif c == 3:
        line()
        choice3(List)
        line()
        execute(List)
    elif c == 4:
        line()
        choice4(List)
        line()
        execute(List)
    elif c == 5:
        line()
        choice5(List)
        line()
        execute(List)
    elif c == 6:
        line()
        choice6(List)
        line()
        execute(List)
    elif c == 7:
        line()
        choice7(List)
        line()
        execute(List)
    elif c == 8:
        line()
        List1 = [1, 2, 3, 4, 5, 6]
        List2 = [2, 3, 4, 5]
        choice8(List1, List2)
        line()
        execute(List)
    else:
        return

if __name__ == '__main__':
    List = list()
    a = int(input('Enter the number of items you want to input in the list: '))
    i = 0
    while i<a:
        List.append(input(f'Enter the {i}th element of the list: '))
        i +=1
    execute(List)
>>>>>>> c7791c941fd996a6ebf78bb2a41ee15944966e00
