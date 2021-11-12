file1 = open("text1.txt","r")
file2 = open("text2.txt","a")
data = file1.readlines()
# print(data)
for i in range(len(data)):
    if i%2!=0 : 
        file2.write(data[i])
file1.close()
file2.close()