n=int(input("enter number of names:"))
names=[]
for i in range(n):
	name=input("enter name:")
	names.append(name)
	names.sort()
for name in names:
	print(name)
