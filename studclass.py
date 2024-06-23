# define a class student
class Student:
    def __init__(self,rno,name,m1,m2,m3):
        self.roll = rno
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

# Calculating total marks
    def calculateTotal(self):
        self.total = self.m1+self.m2+self.m3

# Displaying details of student
    def displayDetails(self):
        print("Roll Number:",self.roll)
        print("Name:",self.name)
        print("marks1:",self.m1)
        print("marks2:",self.m2)
        print("marks3:",self.m3)
        print("Total:",self.total)

# creating object
s1 = Student(3201,"Raju",96,87,99) #student 1
s2 = Student(3202,"Ravi",87,92,95) #student 2

# calling calcluating total func
s1.calculateTotal()
s2.calculateTotal()

# calling displaying details func
s1.displayDetails()
s2.displayDetails()
