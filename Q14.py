file = open("file1.txt","r")
file2 = open("file2.txt","a")
data = file.readlines()
# print(data)
for i in range(len(data)):
    if i%2!=0 : 
        file2.write(data[i])
file.close()
file2.close()