<<<<<<< HEAD
file = open("file1.txt","r")
file2 = open("file2.txt","a")
data = file.readlines()
=======
file1 = open("text1.txt","r")
file2 = open("text2.txt","a")
data = file1.readlines()
>>>>>>> c7791c941fd996a6ebf78bb2a41ee15944966e00
# print(data)
for i in range(len(data)):
    if i%2!=0 : 
        file2.write(data[i])
<<<<<<< HEAD
file.close()
=======
file1.close()
>>>>>>> c7791c941fd996a6ebf78bb2a41ee15944966e00
file2.close()