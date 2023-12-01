n=int(input("enter the number of students:"))
d=int(input("enter the number of working days:"))
s=[]
for i in range(n):
	name=str(input("enter the name of student:"))
	days=int(input("enter the number of present days:"))
	percentage=(days/d)*100
	s.append((percentage,name))
	s.sort(reverse=True)
print(s)

