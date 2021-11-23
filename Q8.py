def ifallnum(l):
    for i in l:
        if type(i)!=int:
            return False
    return True

def numofodd(l):
    if ifallnum(l):
        count=0
        for i in l:
            if i%2!=0:
                count+=1
        return count
    else:
        return False

def largeststr(l):
    if (ifallnum(l))==False:
        lar=""
        for i in l:
            if type(i)==str and len(i)>len(lar):
                lar=i
                print(len(lar),lar)
        return lar
    else:
        return False

def displayreverse(l):
    for i in range(len(l)-1,-1,-1):
        print(l[i],end=",")

def descorder(l):
    n = len(l)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if l[j] < l[j + 1] :
                l[j], l[j + 1] = l[j + 1], l[j]
                

def finditem(l,s):
    a=False
    for i in l:
        if i==s:
            a=True
    return a
    
def removeitem(l,s):
    for i in l:
        if i==s:
            l.remove(s)
            return True
    else:
        return False        

def checkcommon(l,p):
    t=[]
    for i in p:
        if i in l:
            t.append(i)
    return t
    

 
def main():
    l=eval(input("Enter The List - "))
    while True:
        print("---------------------------------------------")
        print("1. Check if All Numbers.")
        print("2. Number of Odd Values.")
        print("3. Display largest String.")
        print("4. Display Reverse.")
        print("5. Find Item.")
        print("6. Remove Item.")
        print("7. Sort in descending order.")
        print("8. Common Members Of 2 Lists.")
        print("9. Exit.")
        while True:
            try:
                a=int(input("Enter Your Choice -----------   "))
                if a>=1 and a<=9:
                    break
            except:
                print("Enter a Number Between 1 and 6")

        print("-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-")
        
        if a==1:
            if (ifallnum(l)):
                print("Yes Only Numbers.")
            else:
                print("No Also Strings")
                
        elif a==2:
            if (numofodd(l)):
                print("No. of Odds - ",numofodd(l))
            else:
                print("Not a Numeric List")
                
        elif a==3:
            if (largeststr(l)):
                print("largest string - ",largeststr(l))
            else:
                print("No String is Present.")
    
        elif a==4:
            print("reverse list - ")
            displayreverse(l)

        elif a==5:
            w=int(input("1. Search Number or 2. Search String - "))
            
            if w==1:
                s=int(input("Enter Int Item - "))
            else:
                s=(input("Enter String Item - "))
            if finditem(l,s):
                print("Item Found.")
            else:
                print("Item Not Found.")
             
        elif a==6:
            s=input("1. Remove Number or 2. Remove String - ")
            if s==1:
                s=int(input("Enter Item - "))
            else:
                s=(input("Enter Item - "))
            if removeitem(l,s):       
                print("Item removed")
            else:
                print("Item Not found in List")
                
        elif a==7:
            if (ifallnum(l)):
                print("Sorted in Descending Order - ")
                descorder(l);
                for i in l:
                    print(i,end=",")
            else:
                print("Error!!!! Strings Present.")
                
        elif a==8:
            p=eval(input("Enter 2nd List"))
            for i in checkcommon(l,p):
                print(i,end=",")

        elif a==9:
            break
            

        print()
        
            

            


main()
