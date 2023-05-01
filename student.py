#Create a Student class and initialize it with name and roll number

class Student:
    def __init__(self,name,rollnumber) -> None:
        self.name=name
        self.rollnumber=rollnumber
    def setAge(self,age):
        self.age=age
    def setMarks(self,marks):
        self.marks=marks
    def display(self):
        print("Name of the student: ",self.name)
        print("rollnumber: ",self.rollnumber)
        print("age: ",self.age)
        print("marks: ",self.marks)
details_of_the_student=Student("Saddam Hussain",333)
details_of_the_student.setAge(25)
details_of_the_student.setMarks(75)
details_of_the_student.display()