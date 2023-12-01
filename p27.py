n = int(input("Enter number of students: "))

y = {}

for i in range(n):

 print("Enter Details of student No.", i+1)

 age = int(input("Age: "))

 name = input("Name: ")

 Grade = (input("Grade: "))

 y[name] = age, Grade

print(y)

l=list(y.items())
l.sort()
print("sorted items in ascending order:",l)
l.sort(reverse=True)
print("sorted items in descending order:",l)
dict=dict(l)

