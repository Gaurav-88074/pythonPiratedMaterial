class Student:
    maxAvg=0
    def __init__(self,name,*marks) :
        self.name = name
        self.marksArray = marks
        self.setMaxAvg(marks)

    def setMaxAvg(self,marks) :
        avg = sum(marks)/len(marks)
        self.avg = avg
        Student.maxAvg = max(Student.maxAvg,avg)

    @staticmethod
    def getMaxAvg():
        return Student.maxAvg
    
    def __str__(self) :
        res = "{0} : {1:.2f}".format(self.name,self.avg)
        return res

student1 = Student("Gaurav",89,90,80)
student2 = Student("Vision",77,99,60)
student3 = Student("Maxx  ",81,50,100)

print(student1)
print()
print(student2)
print()
print(student3)
print()

print("The maximum average marks is : {0:.2f}".format(Student.getMaxAvg()))