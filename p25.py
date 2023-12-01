n = int(input("Enter number of students: "))

student = {}

for i in range(n):

 print("Enter Details of student No.", i+1)

 age = int(input("Age: "))

 name = input("Name: ")

 Grade = (input("Grade: "))

 student[name] = age, Grade

print(student)


