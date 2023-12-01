string=str(input("enter a string")
f=string[0]
r=string[1:]
new=f+r.replace(f,"$")
print(new)
