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
    def __del__(self):
        print("object deleted")

student1 = Student("student1",89,40,80)
student2 = Student("student2",77,99,60)
student3 = Student("student3",81,20,50)

print(student1)
print()
print(student2)
print()
print(student3)
print()

print("The maximum average marks is : {0:.2f}".format(Student.getMaxAvg()))